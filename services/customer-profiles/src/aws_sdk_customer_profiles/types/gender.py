"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Gender``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

Gender: TypeAlias = Literal[
    "MALE",
    "FEMALE",
    "UNSPECIFIED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MALE",
        "FEMALE",
        "UNSPECIFIED",
    )
)


def serialize_json(value: Gender) -> str:
    return value


def deserialize_json(data: str) -> Gender:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Gender value: {data!r}")
    return cast(Gender, data)
