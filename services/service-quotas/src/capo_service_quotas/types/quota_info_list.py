"""Generated from Smithy shape ``com.amazonaws.servicequotas#QuotaInfoList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_quotas.types.quota_info

QuotaInfoList: TypeAlias = list["capo_service_quotas.types.quota_info.QuotaInfo"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QuotaInfoList) -> list:
    import capo_service_quotas.types.quota_info

    out: list = []
    for item in value:
        out.append(capo_service_quotas.types.quota_info.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> QuotaInfoList:
    import capo_service_quotas.types.quota_info

    out: QuotaInfoList = []
    for item in data:
        out.append(capo_service_quotas.types.quota_info.deserialize_aws_json_1_1(item))
    return out
