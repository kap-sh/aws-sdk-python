"""Generated from Smithy shape ``com.amazonaws.iot#GetIndexingConfigurationRequest``."""

from typing_extensions import TypedDict


class GetIndexingConfigurationRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetIndexingConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIndexingConfigurationRequest:
    out: GetIndexingConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
