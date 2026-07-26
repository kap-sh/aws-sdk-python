"""Generated from Smithy shape ``com.amazonaws.qconnect#EmailHeader``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qconnect.types.email_header_key
    import capo_qconnect.types.email_header_value


class EmailHeader(TypedDict, closed=True):
    name: NotRequired["capo_qconnect.types.email_header_key.EmailHeaderKey"]
    """<p>The name of the email header.</p>"""
    value: NotRequired["capo_qconnect.types.email_header_value.EmailHeaderValue"]
    """<p>The value of the email header.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailHeader) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "value" in value:
        out["value"] = value["value"]
    return out


def deserialize_json(data: dict) -> EmailHeader:
    out: EmailHeader = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "value" in data:
        out["value"] = data["value"]
    return out
