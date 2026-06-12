"""Generated from Smithy shape ``com.amazonaws.servicequotas#ServiceQuotaListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.service_quota

ServiceQuotaListDefinition: TypeAlias = list[
    "aws_sdk_service_quotas.types.service_quota.ServiceQuota"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceQuotaListDefinition) -> list:
    import aws_sdk_service_quotas.types.service_quota

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_quotas.types.service_quota.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceQuotaListDefinition:
    import aws_sdk_service_quotas.types.service_quota

    out: ServiceQuotaListDefinition = []
    for item in data:
        out.append(
            aws_sdk_service_quotas.types.service_quota.deserialize_aws_json_1_1(item)
        )
    return out
