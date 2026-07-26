"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#DashboardReferenceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.dashboard_reference

DashboardReferenceList: TypeAlias = list[
    "capo_bcm_dashboards.types.dashboard_reference.DashboardReference"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DashboardReferenceList) -> list:
    import capo_bcm_dashboards.types.dashboard_reference

    out: list = []
    for item in value:
        out.append(
            capo_bcm_dashboards.types.dashboard_reference.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DashboardReferenceList:
    import capo_bcm_dashboards.types.dashboard_reference

    out: DashboardReferenceList = []
    for item in data:
        out.append(
            capo_bcm_dashboards.types.dashboard_reference.deserialize_aws_json_1_0(item)
        )
    return out
