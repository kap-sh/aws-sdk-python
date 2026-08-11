"""Shared service-error runtime.

Hand-written, not regenerated. Helpers for extracting error metadata
from HTTP error responses.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from zapros import Response

if TYPE_CHECKING:
    from xml.etree.ElementTree import Element


def find_error_element(root: Element) -> Element:
    """Return the element holding the error structure's members.

    Handles the three XML error envelopes: a bare ``<Error>`` root
    (restXml with ``noErrorWrapping``), an ``<ErrorResponse><Error>``
    wrapper (restXml/awsQuery), and the ec2Query
    ``<Response><Errors><Error>`` envelope. Falls back to ``root``
    when no ``<Error>`` element is found.
    """
    if root.tag.endswith("Error"):
        return root
    for path in ("Error", "Errors/Error"):
        err = root.find(path)
        if err is not None:
            return err
    return root


def parse_error_metadata(root: Element) -> tuple[str | None, str | None]:
    """Return ``(code, message)`` from an XML error envelope.

    Accepts any envelope understood by :func:`find_error_element`.
    Missing children yield ``None``.
    """
    err = find_error_element(root)
    code_el = err.find("Code")
    msg_el = err.find("Message")
    code = code_el.text if code_el is not None else None
    message = msg_el.text if msg_el is not None else None
    return code, message


def parse_error_metadata_json(
    response: Response, data: dict
) -> tuple[str | None, str | None]:
    """Return ``(code, message)`` from a restJson1 error response.

    Code precedence: the ``X-Amzn-Errortype`` response header, then the
    ``__type`` body field, then ``code``. The raw value is normalized by
    dropping a trailing ``:uri`` suffix first, then a ``prefix#``
    namespace — in that order, so a ``#`` inside the uri suffix cannot
    hijack the code. Message comes from ``message`` or ``Message``.
    Missing values yield ``None``.
    """
    code = (
        response.headers.get("X-Amzn-Errortype")
        or data.get("__type")
        or data.get("code")
    )
    if code is not None:
        code = code.split(":", 1)[0].rsplit("#", 1)[-1]
    message = data.get("message") or data.get("Message")
    return code, message


__all__ = [
    "find_error_element",
    "parse_error_metadata",
    "parse_error_metadata_json",
]
