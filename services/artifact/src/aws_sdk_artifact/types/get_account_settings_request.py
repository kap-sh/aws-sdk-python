"""Generated from Smithy shape ``com.amazonaws.artifact#GetAccountSettingsRequest``."""

from typing_extensions import TypedDict


class GetAccountSettingsRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountSettingsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccountSettingsRequest:
    out: GetAccountSettingsRequest = {}  # type: ignore[typeddict-item]
    return out
