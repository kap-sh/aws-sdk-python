"""Generated from Smithy shape ``com.amazonaws.guardduty#ProfileType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

ProfileType: TypeAlias = Literal["FREQUENCY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("FREQUENCY",))


def serialize_json(value: ProfileType) -> str:
    return value


def deserialize_json(data: str) -> ProfileType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProfileType value: {data!r}")
    return cast(ProfileType, data)
