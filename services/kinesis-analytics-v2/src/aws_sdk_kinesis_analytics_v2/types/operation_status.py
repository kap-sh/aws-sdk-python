"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#OperationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

"""<p>The status of the operation.</p>"""
OperationStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "CANCELLED",
    "SUCCESSFUL",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IN_PROGRESS",
        "CANCELLED",
        "SUCCESSFUL",
        "FAILED",
    )
)


def serialize_aws_json_1_1(value: OperationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OperationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OperationStatus value: {data!r}")
    return cast(OperationStatus, data)
