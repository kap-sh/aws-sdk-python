"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsCcDescriptor``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Cc Descriptor"""
M2tsCcDescriptor: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_json(value: M2tsCcDescriptor) -> str:
    return value


def deserialize_json(data: str) -> M2tsCcDescriptor:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsCcDescriptor value: {data!r}")
    return cast(M2tsCcDescriptor, data)
