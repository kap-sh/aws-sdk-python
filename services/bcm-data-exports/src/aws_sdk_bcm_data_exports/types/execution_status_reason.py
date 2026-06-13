"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExecutionStatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_data_exports.errors import DeserializationError

ExecutionStatusReason: TypeAlias = Literal[
    "INSUFFICIENT_PERMISSION",
    "BILL_OWNER_CHANGED",
    "INTERNAL_FAILURE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INSUFFICIENT_PERMISSION",
        "BILL_OWNER_CHANGED",
        "INTERNAL_FAILURE",
    )
)


def serialize_aws_json_1_1(value: ExecutionStatusReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionStatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatusReason value: {data!r}")
    return cast(ExecutionStatusReason, data)
