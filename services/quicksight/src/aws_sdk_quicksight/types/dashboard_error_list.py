"""Generated from Smithy shape ``com.amazonaws.quicksight#DashboardErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dashboard_error

DashboardErrorList: TypeAlias = list[
    "aws_sdk_quicksight.types.dashboard_error.DashboardError"
]


# --- restJson1 ser/de ---
def serialize_json(value: DashboardErrorList) -> list:
    import aws_sdk_quicksight.types.dashboard_error

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.dashboard_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> DashboardErrorList:
    import aws_sdk_quicksight.types.dashboard_error

    out: DashboardErrorList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.dashboard_error.deserialize_json(item))
    return out
