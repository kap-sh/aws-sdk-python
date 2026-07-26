"""Generated from Smithy shape ``com.amazonaws.outposts#FormFactor``."""

from typing import Literal, TypeAlias, cast

FormFactor: TypeAlias = Literal[
    "RACK",
    "SERVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: FormFactor) -> str:
    return value


def deserialize_json(data: str) -> FormFactor:
    return cast(FormFactor, data)
