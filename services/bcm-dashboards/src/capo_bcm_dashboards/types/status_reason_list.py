"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#StatusReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bcm_dashboards.types.status_reason

StatusReasonList: TypeAlias = list[
    "capo_bcm_dashboards.types.status_reason.StatusReason"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatusReasonList) -> list:
    import capo_bcm_dashboards.types.status_reason

    out: list = []
    for item in value:
        out.append(capo_bcm_dashboards.types.status_reason.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> StatusReasonList:
    import capo_bcm_dashboards.types.status_reason

    out: StatusReasonList = []
    for item in data:
        out.append(
            capo_bcm_dashboards.types.status_reason.deserialize_aws_json_1_0(item)
        )
    return out
