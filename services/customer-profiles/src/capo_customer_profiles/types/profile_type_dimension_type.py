"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileTypeDimensionType``."""

from typing import Literal, TypeAlias, cast

ProfileTypeDimensionType: TypeAlias = Literal[
    "INCLUSIVE",
    "EXCLUSIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileTypeDimensionType) -> str:
    return value


def deserialize_json(data: str) -> ProfileTypeDimensionType:
    return cast(ProfileTypeDimensionType, data)
