"""Generated from Smithy shape ``com.amazonaws.lambda#GetEventSourceMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_lambda.types.string


class GetEventSourceMappingRequest(TypedDict, closed=True):
    uuid: "aws_sdk_lambda.types.string.String"
    """<p>The identifier of the event source mapping.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEventSourceMappingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetEventSourceMappingRequest:
    out: GetEventSourceMappingRequest = {}  # type: ignore[typeddict-item]
    return out
