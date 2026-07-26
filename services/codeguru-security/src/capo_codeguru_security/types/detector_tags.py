"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#DetectorTags``."""

from typing import TypeAlias

DetectorTags: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: DetectorTags) -> list:
    return list(value)


def deserialize_json(data: list) -> DetectorTags:
    return list(data)
