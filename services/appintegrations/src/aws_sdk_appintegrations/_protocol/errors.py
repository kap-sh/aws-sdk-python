"""Shared service-error runtime.

Hand-written, not regenerated. Helpers for extracting error metadata
from HTTP error responses.
"""

from __future__ import annotations

from typing import TYPE_CHECKING
from zapros import Response

if TYPE_CHECKING:
    from xml.etree.ElementTree import Element


def parse_error_metadata(root: Element) -> tuple[str | None, str | None]:
    """Return ``(code, message)`` from a restXml error envelope.

    Accepts either an ``<Error>`` element directly or an
    ``<ErrorResponse>`` wrapper whose first ``<Error>`` child holds the
    metadata. Missing children yield ``None``.
    """
    err = root if root.tag.endswith("Error") else root.find("Error")
    if err is None:
        return None, None
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
    dropping a ``prefix#`` namespace and a trailing ``:uri`` suffix.
    Message comes from ``message`` or ``Message``. Missing values yield
    ``None``.
    """
    code = (
        response.headers.get("X-Amzn-Errortype")
        or data.get("__type")
        or data.get("code")
    )
    if code is not None:
        code = code.rsplit("#", 1)[-1].split(":", 1)[0]
    message = data.get("message") or data.get("Message")
    return code, message


__all__ = [
    "parse_error_metadata",
    "parse_error_metadata_json",
]
