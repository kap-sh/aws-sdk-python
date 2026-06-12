"""Generated from Smithy shape ``com.amazonaws.workspacesthinclient#ApplyTimeOf``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces_thin_client.errors import DeserializationError

ApplyTimeOf: TypeAlias = Literal[
    "UTC",
    "DEVICE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UTC",
        "DEVICE",
    )
)


def serialize_json(value: ApplyTimeOf) -> str:
    return value


def deserialize_json(data: str) -> ApplyTimeOf:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ApplyTimeOf value: {data!r}")
    return cast(ApplyTimeOf, data)
