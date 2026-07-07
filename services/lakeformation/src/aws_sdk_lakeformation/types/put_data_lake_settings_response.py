"""Generated from Smithy shape ``com.amazonaws.lakeformation#PutDataLakeSettingsResponse``."""

from typing_extensions import TypedDict


class PutDataLakeSettingsResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutDataLakeSettingsResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutDataLakeSettingsResponse:
    out: PutDataLakeSettingsResponse = {}  # type: ignore[typeddict-item]
    return out
