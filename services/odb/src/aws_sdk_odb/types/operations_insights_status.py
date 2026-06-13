"""Generated from Smithy shape ``com.amazonaws.odb#OperationsInsightsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

OperationsInsightsStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "NOT_ENABLED",
    "FAILED_ENABLING",
    "FAILED_DISABLING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "NOT_ENABLED",
        "FAILED_ENABLING",
        "FAILED_DISABLING",
    )
)


def serialize_aws_json_1_0(value: OperationsInsightsStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OperationsInsightsStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationsInsightsStatus value: {data!r}")
    return cast(OperationsInsightsStatus, data)
