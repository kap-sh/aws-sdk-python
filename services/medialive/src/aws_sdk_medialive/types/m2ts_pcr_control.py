"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsPcrControl``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Pcr Control"""
M2tsPcrControl: TypeAlias = Literal[
    "CONFIGURED_PCR_PERIOD",
    "PCR_EVERY_PES_PACKET",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CONFIGURED_PCR_PERIOD",
        "PCR_EVERY_PES_PACKET",
    )
)


def serialize_json(value: M2tsPcrControl) -> str:
    return value


def deserialize_json(data: str) -> M2tsPcrControl:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsPcrControl value: {data!r}")
    return cast(M2tsPcrControl, data)
