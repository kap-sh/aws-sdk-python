"""Generated from Smithy shape ``com.amazonaws.cloudtrail#Dashboards``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.dashboard_detail

Dashboards: TypeAlias = list["capo_cloudtrail.types.dashboard_detail.DashboardDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Dashboards) -> list:
    import capo_cloudtrail.types.dashboard_detail

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.dashboard_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Dashboards:
    import capo_cloudtrail.types.dashboard_detail

    out: Dashboards = []
    for item in data:
        out.append(
            capo_cloudtrail.types.dashboard_detail.deserialize_aws_json_1_1(item)
        )
    return out
