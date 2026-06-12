"""Generated from Smithy shape ``com.amazonaws.bedrock#DeleteCustomModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.model_identifier


class DeleteCustomModelRequest(TypedDict):
    model_identifier: "aws_sdk_bedrock.types.model_identifier.ModelIdentifier"
    """<p>Name of the model to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCustomModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteCustomModelRequest:
    out: DeleteCustomModelRequest = {}  # type: ignore[typeddict-item]
    return out
