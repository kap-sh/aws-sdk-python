"""Generated from Smithy shape ``com.amazonaws.servicequotas#ExclusionQuotaList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_quotas.types.excluded_service
    import capo_service_quotas.types.quota_info_list

ExclusionQuotaList: TypeAlias = dict[
    "capo_service_quotas.types.excluded_service.ExcludedService",
    "capo_service_quotas.types.quota_info_list.QuotaInfoList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ExclusionQuotaList) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_service_quotas.types.quota_info_list

        out[key] = capo_service_quotas.types.quota_info_list.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExclusionQuotaList:
    out: ExclusionQuotaList = {}
    for key, value in data.items():
        import capo_service_quotas.types.quota_info_list

        out[key] = capo_service_quotas.types.quota_info_list.deserialize_aws_json_1_1(
            value
        )
    return out
