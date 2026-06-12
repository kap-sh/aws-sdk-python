"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConformancePackStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_config_service.types.organization_conformance_pack_status

OrganizationConformancePackStatuses: TypeAlias = list[
    "aws_sdk_config_service.types.organization_conformance_pack_status.OrganizationConformancePackStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConformancePackStatuses) -> list:
    import aws_sdk_config_service.types.organization_conformance_pack_status

    out: list = []
    for item in value:
        out.append(
            aws_sdk_config_service.types.organization_conformance_pack_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationConformancePackStatuses:
    import aws_sdk_config_service.types.organization_conformance_pack_status

    out: OrganizationConformancePackStatuses = []
    for item in data:
        out.append(
            aws_sdk_config_service.types.organization_conformance_pack_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
