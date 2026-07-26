"""Generated from Smithy shape ``com.amazonaws.bedrock#PutModelInvocationLoggingConfigurationResponse``."""

from typing_extensions import TypedDict


class PutModelInvocationLoggingConfigurationResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutModelInvocationLoggingConfigurationResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutModelInvocationLoggingConfigurationResponse:
    out: PutModelInvocationLoggingConfigurationResponse = {}  # type: ignore[typeddict-item]
    return out
