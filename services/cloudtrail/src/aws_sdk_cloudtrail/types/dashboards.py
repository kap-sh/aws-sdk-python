"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Dashboards``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cloudtrail.types.dashboard_detail

Dashboards: TypeAlias = list[
    "aws_sdk_cloudtrail.types.dashboard_detail.DashboardDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Dashboards) -> list:
    import aws_sdk_cloudtrail.types.dashboard_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cloudtrail.types.dashboard_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Dashboards:
    import aws_sdk_cloudtrail.types.dashboard_detail

    out: Dashboards = []
    for item in data:
        out.append(
            aws_sdk_cloudtrail.types.dashboard_detail.deserialize_aws_json_1_1(item)
        )
    return out
