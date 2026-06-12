"""Generated from Smithy shape ``com.amazonaws.servicequotas#QuotaUtilizationInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.quota_utilization_info

QuotaUtilizationInfoList: TypeAlias = list[
    "aws_sdk_service_quotas.types.quota_utilization_info.QuotaUtilizationInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuotaUtilizationInfoList) -> list:
    import aws_sdk_service_quotas.types.quota_utilization_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_quotas.types.quota_utilization_info.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> QuotaUtilizationInfoList:
    import aws_sdk_service_quotas.types.quota_utilization_info

    out: QuotaUtilizationInfoList = []
    for item in data:
        out.append(
            aws_sdk_service_quotas.types.quota_utilization_info.deserialize_aws_json_1_1(
                item
            )
        )
    return out
