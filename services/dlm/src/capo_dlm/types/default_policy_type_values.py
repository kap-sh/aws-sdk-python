"""Generated from Smithy shape ``com.amazonaws.dlm#DefaultPolicyTypeValues``."""

from typing import Literal, TypeAlias, cast

DefaultPolicyTypeValues: TypeAlias = Literal[
    "VOLUME",
    "INSTANCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DefaultPolicyTypeValues) -> str:
    return value


def deserialize_json(data: str) -> DefaultPolicyTypeValues:
    return cast(DefaultPolicyTypeValues, data)
