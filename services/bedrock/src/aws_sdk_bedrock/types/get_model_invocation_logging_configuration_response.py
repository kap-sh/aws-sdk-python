"""Generated from Smithy shape ``com.amazonaws.bedrock#GetModelInvocationLoggingConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.logging_config


class GetModelInvocationLoggingConfigurationResponse(TypedDict):
    logging_config: NotRequired["aws_sdk_bedrock.types.logging_config.LoggingConfig"]
    """<p>The current configuration values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetModelInvocationLoggingConfigurationResponse) -> dict:
    out: dict = {}
    if "logging_config" in value:
        import aws_sdk_bedrock.types.logging_config

        out["loggingConfig"] = aws_sdk_bedrock.types.logging_config.serialize_json(
            value["logging_config"]
        )
    return out


def deserialize_json(data: dict) -> GetModelInvocationLoggingConfigurationResponse:
    out: GetModelInvocationLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "loggingConfig" in data:
        import aws_sdk_bedrock.types.logging_config

        out["logging_config"] = aws_sdk_bedrock.types.logging_config.deserialize_json(
            data["loggingConfig"]
        )
    return out
