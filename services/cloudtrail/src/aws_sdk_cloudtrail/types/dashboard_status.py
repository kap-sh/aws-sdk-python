"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DashboardStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

DashboardStatus: TypeAlias = Literal[
    "CREATING",
    "CREATED",
    "UPDATING",
    "UPDATED",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATED",
        "UPDATING",
        "UPDATED",
        "DELETING",
    )
)


def serialize_aws_json_1_1(value: DashboardStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DashboardStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashboardStatus value: {data!r}")
    return cast(DashboardStatus, data)
