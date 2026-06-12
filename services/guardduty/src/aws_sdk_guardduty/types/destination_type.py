"""Generated from Smithy shape ``com.amazonaws.guardduty#DestinationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_guardduty.errors import DeserializationError

DestinationType: TypeAlias = Literal["S3",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("S3",))


def serialize_json(value: DestinationType) -> str:
    return value


def deserialize_json(data: str) -> DestinationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DestinationType value: {data!r}")
    return cast(DestinationType, data)
