"""Generated from Smithy shape ``com.amazonaws.backup#DescribeRegionSettingsInput``."""

from typing_extensions import TypedDict


class DescribeRegionSettingsInput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DescribeRegionSettingsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeRegionSettingsInput:
    out: DescribeRegionSettingsInput = {}  # type: ignore[typeddict-item]
    return out
