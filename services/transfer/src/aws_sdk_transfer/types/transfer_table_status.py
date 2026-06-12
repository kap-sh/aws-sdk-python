"""Generated from Smithy shape ``com.amazonaws.transfer#TransferTableStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

TransferTableStatus: TypeAlias = Literal[
    "QUEUED",
    "IN_PROGRESS",
    "COMPLETED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "QUEUED",
        "IN_PROGRESS",
        "COMPLETED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: TransferTableStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TransferTableStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TransferTableStatus value: {data!r}")
    return cast(TransferTableStatus, data)
