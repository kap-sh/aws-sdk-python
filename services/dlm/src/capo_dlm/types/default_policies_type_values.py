"""Generated from Smithy shape ``com.amazonaws.dlm#DefaultPoliciesTypeValues``."""

from typing import Literal, TypeAlias, cast

DefaultPoliciesTypeValues: TypeAlias = Literal[
    "VOLUME",
    "INSTANCE",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: DefaultPoliciesTypeValues) -> str:
    return value


def deserialize_json(data: str) -> DefaultPoliciesTypeValues:
    return cast(DefaultPoliciesTypeValues, data)
