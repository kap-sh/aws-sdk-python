"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#AsyncInvokeSummaries``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_bedrock_runtime.types.async_invoke_summary

AsyncInvokeSummaries: TypeAlias = list["aws_sdk_bedrock_runtime.types.async_invoke_summary.AsyncInvokeSummary"]


# --- restJson1 ser/de ---
def serialize_json(value: AsyncInvokeSummaries) -> list:
    import aws_sdk_bedrock_runtime.types.async_invoke_summary
    out: list = []
    for item in value:
        out.append(aws_sdk_bedrock_runtime.types.async_invoke_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> AsyncInvokeSummaries:
    import aws_sdk_bedrock_runtime.types.async_invoke_summary
    out: AsyncInvokeSummaries = []
    for item in data:
        out.append(aws_sdk_bedrock_runtime.types.async_invoke_summary.deserialize_json(item))
    return out