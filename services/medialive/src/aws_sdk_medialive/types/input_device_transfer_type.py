"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceTransferType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""The type of device transfer. INCOMING for an input device that is being transferred to you, OUTGOING for an input device that you are transferring to another AWS account."""
InputDeviceTransferType: TypeAlias = Literal[
    "OUTGOING",
    "INCOMING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OUTGOING",
        "INCOMING",
    )
)


def serialize_json(value: InputDeviceTransferType) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceTransferType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InputDeviceTransferType value: {data!r}")
    return cast(InputDeviceTransferType, data)
