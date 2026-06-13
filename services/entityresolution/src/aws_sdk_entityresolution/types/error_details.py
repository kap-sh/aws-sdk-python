"""Generated from Smithy shape ``com.amazonaws.entityresolution#ErrorDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.error_message


class ErrorDetails(TypedDict):
    error_message: NotRequired[
        "aws_sdk_entityresolution.types.error_message.ErrorMessage"
    ]
    """<p>The error message from the job, if there is one.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ErrorDetails) -> dict:
    out: dict = {}
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> ErrorDetails:
    out: ErrorDetails = {}  # type: ignore[typeddict-item]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
