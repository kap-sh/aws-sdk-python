"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#StreamDeliveryResource``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.kinesis_resource


class _StreamDeliveryResource_kinesis(TypedDict, closed=True):
    kinesis: "aws_sdk_bedrock_agentcore_control.types.kinesis_resource.KinesisResource"


StreamDeliveryResource: TypeAlias = _StreamDeliveryResource_kinesis


# --- restJson1 ser/de ---
def serialize_json(value: StreamDeliveryResource) -> dict:
    if "kinesis" in value:
        import aws_sdk_bedrock_agentcore_control.types.kinesis_resource

        return {
            "kinesis": aws_sdk_bedrock_agentcore_control.types.kinesis_resource.serialize_json(
                value["kinesis"]
            )
        }
    else:
        raise SerializationError("StreamDeliveryResource: no variant present")


def deserialize_json(data: dict) -> StreamDeliveryResource:
    if "kinesis" in data:
        import aws_sdk_bedrock_agentcore_control.types.kinesis_resource

        return {
            "kinesis": aws_sdk_bedrock_agentcore_control.types.kinesis_resource.deserialize_json(
                data["kinesis"]
            )
        }
    else:
        raise DeserializationError("StreamDeliveryResource: no recognized variant key")
