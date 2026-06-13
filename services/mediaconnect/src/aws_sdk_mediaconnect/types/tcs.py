"""Generated from Smithy shape ``com.amazonaws.mediaconnect#Tcs``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconnect.errors import DeserializationError

Tcs: TypeAlias = Literal[
    "SDR",
    "PQ",
    "HLG",
    "LINEAR",
    "BT2100LINPQ",
    "BT2100LINHLG",
    "ST2065-1",
    "ST428-1",
    "DENSITY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SDR",
        "PQ",
        "HLG",
        "LINEAR",
        "BT2100LINPQ",
        "BT2100LINHLG",
        "ST2065-1",
        "ST428-1",
        "DENSITY",
    )
)


def serialize_json(value: Tcs) -> str:
    return value


def deserialize_json(data: str) -> Tcs:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Tcs value: {data!r}")
    return cast(Tcs, data)
