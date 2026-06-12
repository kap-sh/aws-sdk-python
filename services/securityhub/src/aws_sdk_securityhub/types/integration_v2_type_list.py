"""Generated from Smithy shape ``com.amazonaws.securityhub#IntegrationV2TypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integration_v2_type

IntegrationV2TypeList: TypeAlias = list[
    "aws_sdk_securityhub.types.integration_v2_type.IntegrationV2Type"
]


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationV2TypeList) -> list:
    import aws_sdk_securityhub.types.integration_v2_type

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.integration_v2_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> IntegrationV2TypeList:
    import aws_sdk_securityhub.types.integration_v2_type

    out: IntegrationV2TypeList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.integration_v2_type.deserialize_json(item))
    return out
