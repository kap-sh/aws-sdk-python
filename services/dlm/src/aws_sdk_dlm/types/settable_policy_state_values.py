"""Generated from Smithy shape ``com.amazonaws.dlm#SettablePolicyStateValues``."""

from typing import Literal, TypeAlias, cast

SettablePolicyStateValues: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SettablePolicyStateValues) -> str:
    return value


def deserialize_json(data: str) -> SettablePolicyStateValues:
    return cast(SettablePolicyStateValues, data)
