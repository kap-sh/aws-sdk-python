"""Generated from Smithy shape ``com.amazonaws.ssmincidents#SsmParameterValues``."""

from typing import TypeAlias

SsmParameterValues: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: SsmParameterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> SsmParameterValues:
    return list(data)
