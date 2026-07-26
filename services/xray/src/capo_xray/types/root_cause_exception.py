"""Generated from Smithy shape ``com.amazonaws.xray#RootCauseException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.string


class RootCauseException(TypedDict, closed=True):
    name: NotRequired["capo_xray.types.string.String"]
    """<p>The name of the exception.</p>"""
    message: NotRequired["capo_xray.types.string.String"]
    """<p>The message of the exception.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RootCauseException) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> RootCauseException:
    out: RootCauseException = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
