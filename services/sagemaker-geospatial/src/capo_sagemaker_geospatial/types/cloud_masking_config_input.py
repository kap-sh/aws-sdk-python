"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#CloudMaskingConfigInput``."""

from typing_extensions import TypedDict


class CloudMaskingConfigInput(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CloudMaskingConfigInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CloudMaskingConfigInput:
    out: CloudMaskingConfigInput = {}  # type: ignore[typeddict-item]
    return out
