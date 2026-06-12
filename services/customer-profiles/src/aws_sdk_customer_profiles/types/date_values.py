"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DateValues``."""

from typing import TypeAlias

DateValues: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: DateValues) -> list:
    return list(value)


def deserialize_json(data: list) -> DateValues:
    return list(data)
