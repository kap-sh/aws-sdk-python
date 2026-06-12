"""Generated from Smithy shape ``com.amazonaws.servicequotas#RequestedServiceQuotaChangeHistoryListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.requested_service_quota_change

RequestedServiceQuotaChangeHistoryListDefinition: TypeAlias = list[
    "aws_sdk_service_quotas.types.requested_service_quota_change.RequestedServiceQuotaChange"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: RequestedServiceQuotaChangeHistoryListDefinition,
) -> list:
    import aws_sdk_service_quotas.types.requested_service_quota_change

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_quotas.types.requested_service_quota_change.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: list,
) -> RequestedServiceQuotaChangeHistoryListDefinition:
    import aws_sdk_service_quotas.types.requested_service_quota_change

    out: RequestedServiceQuotaChangeHistoryListDefinition = []
    for item in data:
        out.append(
            aws_sdk_service_quotas.types.requested_service_quota_change.deserialize_aws_json_1_1(
                item
            )
        )
    return out
