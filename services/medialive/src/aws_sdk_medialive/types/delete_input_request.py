"""Generated from Smithy shape ``com.amazonaws.medialive#DeleteInputRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_medialive.types.__string


class DeleteInputRequest(TypedDict):
    input_id: "aws_sdk_medialive.types.__string.__string"
    """Unique ID of the input"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteInputRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteInputRequest:
    out: DeleteInputRequest = {}  # type: ignore[typeddict-item]
    return out
