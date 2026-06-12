"""Generated from Smithy shape ``com.amazonaws.servicequotas#ServiceInfoListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_quotas.types.service_info

ServiceInfoListDefinition: TypeAlias = list[
    "aws_sdk_service_quotas.types.service_info.ServiceInfo"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceInfoListDefinition) -> list:
    import aws_sdk_service_quotas.types.service_info

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_quotas.types.service_info.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ServiceInfoListDefinition:
    import aws_sdk_service_quotas.types.service_info

    out: ServiceInfoListDefinition = []
    for item in data:
        out.append(
            aws_sdk_service_quotas.types.service_info.deserialize_aws_json_1_1(item)
        )
    return out
