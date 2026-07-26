"""Generated from Smithy shape ``com.amazonaws.servicequotas#ExclusionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_quotas.types.excluded_quota_list
    import capo_service_quotas.types.excluded_service

ExclusionList: TypeAlias = dict[
    "capo_service_quotas.types.excluded_service.ExcludedService",
    "capo_service_quotas.types.excluded_quota_list.ExcludedQuotaList",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ExclusionList) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_service_quotas.types.excluded_quota_list

        out[key] = capo_service_quotas.types.excluded_quota_list.serialize_aws_json_1_1(
            value
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExclusionList:
    out: ExclusionList = {}
    for key, value in data.items():
        import capo_service_quotas.types.excluded_quota_list

        out[key] = (
            capo_service_quotas.types.excluded_quota_list.deserialize_aws_json_1_1(
                value
            )
        )
    return out
