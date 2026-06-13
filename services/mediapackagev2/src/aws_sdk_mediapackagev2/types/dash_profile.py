"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashProfile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

DashProfile: TypeAlias = Literal["DVB_DASH",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DVB_DASH",))


def serialize_json(value: DashProfile) -> str:
    return value


def deserialize_json(data: str) -> DashProfile:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashProfile value: {data!r}")
    return cast(DashProfile, data)
