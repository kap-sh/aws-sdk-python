"""Generated from Smithy shape ``com.amazonaws.bedrock#InvocationLogsConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.invocation_log_source
    import aws_sdk_bedrock.types.request_metadata_filters
    import aws_sdk_bedrock.types.use_prompt_response


class InvocationLogsConfig(TypedDict):
    use_prompt_response: "aws_sdk_bedrock.types.use_prompt_response.UsePromptResponse"
    """<p>Whether to use the model's response for training, or just the prompt. The default value is <code>False</code>.</p>"""
    invocation_log_source: (
        "aws_sdk_bedrock.types.invocation_log_source.InvocationLogSource"
    )
    """<p>The source of the invocation logs.</p>"""
    request_metadata_filters: NotRequired[
        "aws_sdk_bedrock.types.request_metadata_filters.RequestMetadataFilters"
    ]
    """<p>Rules for filtering invocation logs based on request metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvocationLogsConfig) -> dict:
    out: dict = {}
    out["usePromptResponse"] = value.get("use_prompt_response", False)
    import aws_sdk_bedrock.types.invocation_log_source

    out["invocationLogSource"] = (
        aws_sdk_bedrock.types.invocation_log_source.serialize_json(
            value["invocation_log_source"]
        )
    )
    if "request_metadata_filters" in value:
        import aws_sdk_bedrock.types.request_metadata_filters

        out["requestMetadataFilters"] = (
            aws_sdk_bedrock.types.request_metadata_filters.serialize_json(
                value["request_metadata_filters"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvocationLogsConfig:
    out: InvocationLogsConfig = {}  # type: ignore[typeddict-item]
    if "usePromptResponse" in data:
        out["use_prompt_response"] = data["usePromptResponse"]
    else:
        out["use_prompt_response"] = False
    if "invocationLogSource" in data:
        import aws_sdk_bedrock.types.invocation_log_source

        out["invocation_log_source"] = (
            aws_sdk_bedrock.types.invocation_log_source.deserialize_json(
                data["invocationLogSource"]
            )
        )
    else:
        raise DeserializationError(
            "InvocationLogsConfig.invocation_log_source required"
        )
    if "requestMetadataFilters" in data:
        import aws_sdk_bedrock.types.request_metadata_filters

        out["request_metadata_filters"] = (
            aws_sdk_bedrock.types.request_metadata_filters.deserialize_json(
                data["requestMetadataFilters"]
            )
        )
    return out
