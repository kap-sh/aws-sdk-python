"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DisassociatedDataStorageState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

DisassociatedDataStorageState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_json(value: DisassociatedDataStorageState) -> str:
    return value


def deserialize_json(data: str) -> DisassociatedDataStorageState:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DisassociatedDataStorageState value: {data!r}"
        )
    return cast(DisassociatedDataStorageState, data)
