"""Generated from Smithy shape ``com.amazonaws.osis#ValidationMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_osis.types.string


class ValidationMessage(TypedDict, closed=True):
    message: NotRequired["aws_sdk_osis.types.string.String"]
    """<p>The validation message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationMessage) -> dict:
    out: dict = {}
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> ValidationMessage:
    out: ValidationMessage = {}  # type: ignore[typeddict-item]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
