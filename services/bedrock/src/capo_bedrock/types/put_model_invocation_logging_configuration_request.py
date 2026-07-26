"""Generated from Smithy shape ``com.amazonaws.bedrock#PutModelInvocationLoggingConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock.types.logging_config


class PutModelInvocationLoggingConfigurationRequest(TypedDict, closed=True):
    logging_config: "capo_bedrock.types.logging_config.LoggingConfig"
    """<p>The logging configuration values to set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutModelInvocationLoggingConfigurationRequest) -> dict:
    out: dict = {}
    import capo_bedrock.types.logging_config

    out["loggingConfig"] = capo_bedrock.types.logging_config.serialize_json(
        value["logging_config"]
    )
    return out


def deserialize_json(data: dict) -> PutModelInvocationLoggingConfigurationRequest:
    out: PutModelInvocationLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "loggingConfig" in data:
        import capo_bedrock.types.logging_config

        out["logging_config"] = capo_bedrock.types.logging_config.deserialize_json(
            data["loggingConfig"]
        )
    else:
        raise DeserializationError(
            "PutModelInvocationLoggingConfigurationRequest.logging_config required"
        )
    return out
