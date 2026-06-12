"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConformancePackNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.organization_conformance_pack_name

OrganizationConformancePackNames: TypeAlias = list[
    "aws_sdk_config_service.types.organization_conformance_pack_name.OrganizationConformancePackName"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConformancePackNames) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> OrganizationConformancePackNames:
    return list(data)
