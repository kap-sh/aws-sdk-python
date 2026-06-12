"""Generated from Smithy shape ``com.amazonaws.mediaconvert#RenewalType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""Specifies whether the term of your reserved queue pricing plan is automatically extended (AUTO_RENEW) or expires (EXPIRE) at the end of the term."""
RenewalType: TypeAlias = Literal[
    "AUTO_RENEW",
    "EXPIRE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AUTO_RENEW",
        "EXPIRE",
    )
)


def serialize_json(value: RenewalType) -> str:
    return value


def deserialize_json(data: str) -> RenewalType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RenewalType value: {data!r}")
    return cast(RenewalType, data)
