"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ResourceLocation``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.s3_location


class _ResourceLocation_s3(TypedDict):
    s3: "aws_sdk_bedrock_agentcore_control.types.s3_location.S3Location"


ResourceLocation: TypeAlias = _ResourceLocation_s3


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLocation) -> dict:
    if "s3" in value:
        import aws_sdk_bedrock_agentcore_control.types.s3_location

        return {
            "s3": aws_sdk_bedrock_agentcore_control.types.s3_location.serialize_json(
                value["s3"]
            )
        }
    else:
        raise SerializationError("ResourceLocation: no variant present")


def deserialize_json(data: dict) -> ResourceLocation:
    if "s3" in data:
        import aws_sdk_bedrock_agentcore_control.types.s3_location

        return {
            "s3": aws_sdk_bedrock_agentcore_control.types.s3_location.deserialize_json(
                data["s3"]
            )
        }
    else:
        raise DeserializationError("ResourceLocation: no recognized variant key")
