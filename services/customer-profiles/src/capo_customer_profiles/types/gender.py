"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Gender``."""

from typing import Literal, TypeAlias, cast

Gender: TypeAlias = Literal[
    "MALE",
    "FEMALE",
    "UNSPECIFIED",
]


# --- restJson1 ser/de ---
def serialize_json(value: Gender) -> str:
    return value


def deserialize_json(data: str) -> Gender:
    return cast(Gender, data)
