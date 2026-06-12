"""Generated from Smithy shape ``com.amazonaws.bedrock#PutModelInvocationLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.logging_config


class PutModelInvocationLoggingConfigurationRequest(TypedDict):
    logging_config: "aws_sdk_bedrock.types.logging_config.LoggingConfig"
    """<p>The logging configuration values to set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutModelInvocationLoggingConfigurationRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock.types.logging_config

    out["loggingConfig"] = aws_sdk_bedrock.types.logging_config.serialize_json(
        value["logging_config"]
    )
    return out


def deserialize_json(data: dict) -> PutModelInvocationLoggingConfigurationRequest:
    out: PutModelInvocationLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "loggingConfig" in data:
        import aws_sdk_bedrock.types.logging_config

        out["logging_config"] = aws_sdk_bedrock.types.logging_config.deserialize_json(
            data["loggingConfig"]
        )
    else:
        raise DeserializationError(
            "PutModelInvocationLoggingConfigurationRequest.logging_config required"
        )
    return out
