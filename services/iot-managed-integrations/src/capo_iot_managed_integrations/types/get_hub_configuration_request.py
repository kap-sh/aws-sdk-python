"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetHubConfigurationRequest``."""

from typing_extensions import TypedDict


class GetHubConfigurationRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetHubConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetHubConfigurationRequest:
    out: GetHubConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
