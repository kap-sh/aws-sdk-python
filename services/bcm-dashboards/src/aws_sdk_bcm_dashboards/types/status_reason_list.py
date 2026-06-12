"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#StatusReasonList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bcm_dashboards.types.status_reason

StatusReasonList: TypeAlias = list[
    "aws_sdk_bcm_dashboards.types.status_reason.StatusReason"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatusReasonList) -> list:
    import aws_sdk_bcm_dashboards.types.status_reason

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bcm_dashboards.types.status_reason.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> StatusReasonList:
    import aws_sdk_bcm_dashboards.types.status_reason

    out: StatusReasonList = []
    for item in data:
        out.append(
            aws_sdk_bcm_dashboards.types.status_reason.deserialize_aws_json_1_0(item)
        )
    return out
