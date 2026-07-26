"""Generated from Smithy shape ``com.amazonaws.dlm#GettablePolicyStateValues``."""

from typing import Literal, TypeAlias, cast

GettablePolicyStateValues: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "ERROR",
]


# --- restJson1 ser/de ---
def serialize_json(value: GettablePolicyStateValues) -> str:
    return value


def deserialize_json(data: str) -> GettablePolicyStateValues:
    return cast(GettablePolicyStateValues, data)
