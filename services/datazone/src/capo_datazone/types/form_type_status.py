"""Generated from Smithy shape ``com.amazonaws.datazone#FormTypeStatus``."""

from typing import Literal, TypeAlias, cast

FormTypeStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FormTypeStatus) -> str:
    return value


def deserialize_json(data: str) -> FormTypeStatus:
    return cast(FormTypeStatus, data)
