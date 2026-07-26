"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ResourceLocation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.s3_location


class _ResourceLocation_s3(TypedDict, closed=True):
    s3: "capo_bedrock_agentcore.types.s3_location.S3Location"


ResourceLocation: TypeAlias = _ResourceLocation_s3


# --- restJson1 ser/de ---
def serialize_json(value: ResourceLocation) -> dict:
    if "s3" in value:
        import capo_bedrock_agentcore.types.s3_location

        return {
            "s3": capo_bedrock_agentcore.types.s3_location.serialize_json(value["s3"])
        }
    else:
        raise SerializationError("ResourceLocation: no variant present")


def deserialize_json(data: dict) -> ResourceLocation:
    if "s3" in data:
        import capo_bedrock_agentcore.types.s3_location

        return {
            "s3": capo_bedrock_agentcore.types.s3_location.deserialize_json(data["s3"])
        }
    else:
        raise DeserializationError("ResourceLocation: no recognized variant key")
