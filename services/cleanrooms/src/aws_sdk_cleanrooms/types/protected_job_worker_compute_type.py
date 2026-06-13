"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedJobWorkerComputeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cleanrooms.errors import DeserializationError

ProtectedJobWorkerComputeType: TypeAlias = Literal[
    "CR.1X",
    "CR.4X",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CR.1X",
        "CR.4X",
    )
)


def serialize_json(value: ProtectedJobWorkerComputeType) -> str:
    return value


def deserialize_json(data: str) -> ProtectedJobWorkerComputeType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProtectedJobWorkerComputeType value: {data!r}"
        )
    return cast(ProtectedJobWorkerComputeType, data)
