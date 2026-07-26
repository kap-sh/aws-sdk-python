"""Generated from Smithy shape ``com.amazonaws.backup#DescribeGlobalSettingsInput``."""

from typing_extensions import TypedDict


class DescribeGlobalSettingsInput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGlobalSettingsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeGlobalSettingsInput:
    out: DescribeGlobalSettingsInput = {}  # type: ignore[typeddict-item]
    return out
