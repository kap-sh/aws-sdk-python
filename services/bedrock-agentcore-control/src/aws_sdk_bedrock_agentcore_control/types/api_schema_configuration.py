"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ApiSchemaConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.s3_configuration
    import aws_sdk_bedrock_agentcore_control.types.inline_payload

class _ApiSchemaConfiguration_s3(TypedDict):
    s3: "aws_sdk_bedrock_agentcore_control.types.s3_configuration.S3Configuration"


class _ApiSchemaConfiguration_inlinePayload(TypedDict):
    inlinePayload: "aws_sdk_bedrock_agentcore_control.types.inline_payload.InlinePayload"

ApiSchemaConfiguration: TypeAlias = _ApiSchemaConfiguration_s3 | _ApiSchemaConfiguration_inlinePayload

# --- restJson1 ser/de ---
def serialize_json(value: ApiSchemaConfiguration) -> dict:
    if "s3" in value:
        import aws_sdk_bedrock_agentcore_control.types.s3_configuration
        return {"s3": aws_sdk_bedrock_agentcore_control.types.s3_configuration.serialize_json(value["s3"])}
    elif "inlinePayload" in value:
        return {"inlinePayload": value["inlinePayload"]}
    else:
        raise SerializationError("ApiSchemaConfiguration: no variant present")


def deserialize_json(data: dict) -> ApiSchemaConfiguration:
    if "s3" in data:
        import aws_sdk_bedrock_agentcore_control.types.s3_configuration
        return {"s3": aws_sdk_bedrock_agentcore_control.types.s3_configuration.deserialize_json(data["s3"])}
    elif "inlinePayload" in data:
        return {"inlinePayload": data["inlinePayload"]}
    else:
        raise DeserializationError("ApiSchemaConfiguration: no recognized variant key")