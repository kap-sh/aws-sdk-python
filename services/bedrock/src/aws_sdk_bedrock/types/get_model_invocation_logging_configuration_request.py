"""Generated from Smithy shape ``com.amazonaws.bedrock#GetModelInvocationLoggingConfigurationRequest``."""

from typing_extensions import TypedDict


class GetModelInvocationLoggingConfigurationRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetModelInvocationLoggingConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetModelInvocationLoggingConfigurationRequest:
    out: GetModelInvocationLoggingConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
