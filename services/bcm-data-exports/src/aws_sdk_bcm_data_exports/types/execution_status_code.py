"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExecutionStatusCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_data_exports.errors import DeserializationError

ExecutionStatusCode: TypeAlias = Literal[
    "INITIATION_IN_PROCESS",
    "QUERY_QUEUED",
    "QUERY_IN_PROCESS",
    "QUERY_FAILURE",
    "DELIVERY_IN_PROCESS",
    "DELIVERY_SUCCESS",
    "DELIVERY_FAILURE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INITIATION_IN_PROCESS",
        "QUERY_QUEUED",
        "QUERY_IN_PROCESS",
        "QUERY_FAILURE",
        "DELIVERY_IN_PROCESS",
        "DELIVERY_SUCCESS",
        "DELIVERY_FAILURE",
    )
)


def serialize_aws_json_1_1(value: ExecutionStatusCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionStatusCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionStatusCode value: {data!r}")
    return cast(ExecutionStatusCode, data)
