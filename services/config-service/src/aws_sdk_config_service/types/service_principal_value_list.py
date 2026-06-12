"""Generated from Smithy shape ``com.amazonaws.configservice#ServicePrincipalValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.service_principal_value

ServicePrincipalValueList: TypeAlias = list[
    "aws_sdk_config_service.types.service_principal_value.ServicePrincipalValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServicePrincipalValueList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ServicePrincipalValueList:
    return list(data)
