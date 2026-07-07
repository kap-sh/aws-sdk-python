"""Generated from Smithy shape ``com.amazonaws.opensearch#GetDefaultApplicationSettingRequest``."""

from typing_extensions import TypedDict


class GetDefaultApplicationSettingRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetDefaultApplicationSettingRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDefaultApplicationSettingRequest:
    out: GetDefaultApplicationSettingRequest = {}  # type: ignore[typeddict-item]
    return out
