"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#DataSourceType``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict
from aws_sdk_bedrock_agentcore_control.errors import DeserializationError, SerializationError
if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.inline_examples_source
    import aws_sdk_bedrock_agentcore_control.types.s3_source

class _DataSourceType_inlineExamples(TypedDict):
    inlineExamples: "aws_sdk_bedrock_agentcore_control.types.inline_examples_source.InlineExamplesSource"


class _DataSourceType_s3Source(TypedDict):
    s3Source: "aws_sdk_bedrock_agentcore_control.types.s3_source.S3Source"

DataSourceType: TypeAlias = _DataSourceType_inlineExamples | _DataSourceType_s3Source

# --- restJson1 ser/de ---
def serialize_json(value: DataSourceType) -> dict:
    if "inlineExamples" in value:
        import aws_sdk_bedrock_agentcore_control.types.inline_examples_source
        return {"inlineExamples": aws_sdk_bedrock_agentcore_control.types.inline_examples_source.serialize_json(value["inlineExamples"])}
    elif "s3Source" in value:
        import aws_sdk_bedrock_agentcore_control.types.s3_source
        return {"s3Source": aws_sdk_bedrock_agentcore_control.types.s3_source.serialize_json(value["s3Source"])}
    else:
        raise SerializationError("DataSourceType: no variant present")


def deserialize_json(data: dict) -> DataSourceType:
    if "inlineExamples" in data:
        import aws_sdk_bedrock_agentcore_control.types.inline_examples_source
        return {"inlineExamples": aws_sdk_bedrock_agentcore_control.types.inline_examples_source.deserialize_json(data["inlineExamples"])}
    elif "s3Source" in data:
        import aws_sdk_bedrock_agentcore_control.types.s3_source
        return {"s3Source": aws_sdk_bedrock_agentcore_control.types.s3_source.deserialize_json(data["s3Source"])}
    else:
        raise DeserializationError("DataSourceType: no recognized variant key")