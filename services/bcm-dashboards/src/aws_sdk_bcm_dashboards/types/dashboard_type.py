"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#DashboardType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_dashboards.errors import DeserializationError

DashboardType: TypeAlias = Literal["CUSTOM",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("CUSTOM",))


def serialize_aws_json_1_0(value: DashboardType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DashboardType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DashboardType value: {data!r}")
    return cast(DashboardType, data)
