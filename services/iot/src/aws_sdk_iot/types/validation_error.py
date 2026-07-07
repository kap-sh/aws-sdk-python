"""Generated from Smithy shape ``com.amazonaws.iot#ValidationError``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.error_message


class ValidationError(TypedDict, closed=True):
    error_message: NotRequired["aws_sdk_iot.types.error_message.ErrorMessage"]
    """<p>The description of an error found in the behaviors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValidationError) -> dict:
    out: dict = {}
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ValidationError:
    out: ValidationError = {}  # type: ignore[typeddict-item]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
