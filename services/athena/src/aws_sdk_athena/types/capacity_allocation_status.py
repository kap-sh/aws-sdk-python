"""Generated from Smithy shape ``com.amazonaws.athena#CapacityAllocationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

CapacityAllocationStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCEEDED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "SUCCEEDED",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: CapacityAllocationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityAllocationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapacityAllocationStatus value: {data!r}")
    return cast(CapacityAllocationStatus, data)
