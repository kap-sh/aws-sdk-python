"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#StatusReason``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bcm_dashboards.errors import DeserializationError

StatusReason: TypeAlias = Literal[
    "DATA_SOURCE_ACCESS_DENIED",
    "EXECUTION_ROLE_ASSUME_FAILED",
    "EXECUTION_ROLE_INSUFFICIENT_PERMISSIONS",
    "DASHBOARD_NOT_FOUND",
    "DASHBOARD_ACCESS_DENIED",
    "INTERNAL_FAILURE",
    "WIDGET_ID_NOT_FOUND",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DATA_SOURCE_ACCESS_DENIED",
        "EXECUTION_ROLE_ASSUME_FAILED",
        "EXECUTION_ROLE_INSUFFICIENT_PERMISSIONS",
        "DASHBOARD_NOT_FOUND",
        "DASHBOARD_ACCESS_DENIED",
        "INTERNAL_FAILURE",
        "WIDGET_ID_NOT_FOUND",
    )
)


def serialize_aws_json_1_0(value: StatusReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StatusReason:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StatusReason value: {data!r}")
    return cast(StatusReason, data)
