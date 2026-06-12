"""Generated from Smithy shape ``com.amazonaws.securityhub#IntegrationTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integration_type

IntegrationTypeList: TypeAlias = list[
    "aws_sdk_securityhub.types.integration_type.IntegrationType"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationTypeList) -> list:
    import aws_sdk_securityhub.types.integration_type

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.integration_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntegrationTypeList:
    import aws_sdk_securityhub.types.integration_type

    out: IntegrationTypeList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.integration_type.deserialize_json(item))
    return out
