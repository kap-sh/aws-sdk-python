"""Generated from Smithy shape ``com.amazonaws.guardduty#ProfileSubtype``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

ProfileSubtype: TypeAlias = Literal[
    "FREQUENT",
    "INFREQUENT",
    "UNSEEN",
    "RARE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FREQUENT",
        "INFREQUENT",
        "UNSEEN",
        "RARE",
    )
)


def serialize_json(value: ProfileSubtype) -> str:
    return value


def deserialize_json(data: str) -> ProfileSubtype:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProfileSubtype value: {data!r}")
    return cast(ProfileSubtype, data)
