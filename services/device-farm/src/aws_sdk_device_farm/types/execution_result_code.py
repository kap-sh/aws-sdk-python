"""Generated from Smithy shape ``com.amazonaws.devicefarm#ExecutionResultCode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_device_farm.errors import DeserializationError

ExecutionResultCode: TypeAlias = Literal[
    "PARSING_FAILED",
    "VPC_ENDPOINT_SETUP_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PARSING_FAILED",
        "VPC_ENDPOINT_SETUP_FAILED",
    )
)


def serialize_aws_json_1_1(value: ExecutionResultCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExecutionResultCode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ExecutionResultCode value: {data!r}")
    return cast(ExecutionResultCode, data)
