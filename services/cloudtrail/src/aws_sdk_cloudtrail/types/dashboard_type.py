"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DashboardType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

DashboardType: TypeAlias = Literal[
    "MANAGED",
    "CUSTOM",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MANAGED",
        "CUSTOM",
    )
)


def serialize_aws_json_1_1(value: DashboardType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DashboardType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashboardType value: {data!r}")
    return cast(DashboardType, data)
