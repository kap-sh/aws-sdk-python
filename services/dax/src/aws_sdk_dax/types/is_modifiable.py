"""Generated from Smithy shape ``com.amazonaws.dax#IsModifiable``."""

from typing import Literal, TypeAlias, cast

IsModifiable: TypeAlias = Literal[
    "TRUE",
    "FALSE",
    "CONDITIONAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IsModifiable) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> IsModifiable:
    return cast(IsModifiable, data)
