"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#DashTtmlProfile``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediapackagev2.errors import DeserializationError

DashTtmlProfile: TypeAlias = Literal[
    "IMSC_1",
    "EBU_TT_D_101",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IMSC_1",
        "EBU_TT_D_101",
    )
)


def serialize_json(value: DashTtmlProfile) -> str:
    return value


def deserialize_json(data: str) -> DashTtmlProfile:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashTtmlProfile value: {data!r}")
    return cast(DashTtmlProfile, data)
