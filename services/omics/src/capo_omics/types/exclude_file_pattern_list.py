"""Generated from Smithy shape ``com.amazonaws.omics#ExcludeFilePatternList``."""

from typing import TypeAlias

ExcludeFilePatternList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ExcludeFilePatternList) -> list:
    return list(value)


def deserialize_json(data: list) -> ExcludeFilePatternList:
    return list(data)
