"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#InvokeModelWithBidirectionalStreamInput``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.bidirectional_input_payload_part


class _InvokeModelWithBidirectionalStreamInput_chunk(TypedDict):
    chunk: "aws_sdk_bedrock_runtime.types.bidirectional_input_payload_part.BidirectionalInputPayloadPart"


InvokeModelWithBidirectionalStreamInput: TypeAlias = (
    _InvokeModelWithBidirectionalStreamInput_chunk
)


# --- restJson1 ser/de ---
def serialize_json(value: InvokeModelWithBidirectionalStreamInput) -> dict:
    if "chunk" in value:
        import aws_sdk_bedrock_runtime.types.bidirectional_input_payload_part

        return {
            "chunk": aws_sdk_bedrock_runtime.types.bidirectional_input_payload_part.serialize_json(
                value["chunk"]
            )
        }
    else:
        raise SerializationError(
            "InvokeModelWithBidirectionalStreamInput: no variant present"
        )


def deserialize_json(data: dict) -> InvokeModelWithBidirectionalStreamInput:
    if "chunk" in data:
        import aws_sdk_bedrock_runtime.types.bidirectional_input_payload_part

        return {
            "chunk": aws_sdk_bedrock_runtime.types.bidirectional_input_payload_part.deserialize_json(
                data["chunk"]
            )
        }
    else:
        raise DeserializationError(
            "InvokeModelWithBidirectionalStreamInput: no recognized variant key"
        )
