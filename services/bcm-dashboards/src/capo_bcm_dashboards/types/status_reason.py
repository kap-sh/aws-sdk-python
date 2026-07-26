"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#StatusReason``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: StatusReason) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StatusReason:
    return cast(StatusReason, data)
