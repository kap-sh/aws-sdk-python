"""Generated from Smithy shape ``com.amazonaws.lambda#DeleteEventSourceMappingRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class DeleteEventSourceMappingRequest(TypedDict):
    uuid: "aws_sdk_lambda.types.string.String"
    """<p>The identifier of the event source mapping.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteEventSourceMappingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteEventSourceMappingRequest:
    out: DeleteEventSourceMappingRequest = {}  # type: ignore[typeddict-item]
    return out
