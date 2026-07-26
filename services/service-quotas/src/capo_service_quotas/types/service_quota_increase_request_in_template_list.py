"""Generated from Smithy shape ``com.amazonaws.servicequotas#ServiceQuotaIncreaseRequestInTemplateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_quotas.types.service_quota_increase_request_in_template

ServiceQuotaIncreaseRequestInTemplateList: TypeAlias = list[
    "capo_service_quotas.types.service_quota_increase_request_in_template.ServiceQuotaIncreaseRequestInTemplate"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceQuotaIncreaseRequestInTemplateList) -> list:
    import capo_service_quotas.types.service_quota_increase_request_in_template

    out: list = []
    for item in value:
        out.append(
            capo_service_quotas.types.service_quota_increase_request_in_template.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceQuotaIncreaseRequestInTemplateList:
    import capo_service_quotas.types.service_quota_increase_request_in_template

    out: ServiceQuotaIncreaseRequestInTemplateList = []
    for item in data:
        out.append(
            capo_service_quotas.types.service_quota_increase_request_in_template.deserialize_aws_json_1_1(
                item
            )
        )
    return out
