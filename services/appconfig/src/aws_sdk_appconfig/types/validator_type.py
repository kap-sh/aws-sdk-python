"""Generated from Smithy shape ``com.amazonaws.appconfig#ValidatorType``."""

from typing import Literal, TypeAlias, cast

ValidatorType: TypeAlias = Literal[
    "JSON_SCHEMA",
    "LAMBDA",
]


# --- restJson1 ser/de ---
def serialize_json(value: ValidatorType) -> str:
    return value


def deserialize_json(data: str) -> ValidatorType:
    return cast(ValidatorType, data)
