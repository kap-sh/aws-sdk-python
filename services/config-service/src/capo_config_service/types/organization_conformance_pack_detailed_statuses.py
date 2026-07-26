"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConformancePackDetailedStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.organization_conformance_pack_detailed_status

OrganizationConformancePackDetailedStatuses: TypeAlias = list[
    "capo_config_service.types.organization_conformance_pack_detailed_status.OrganizationConformancePackDetailedStatus"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConformancePackDetailedStatuses) -> list:
    import capo_config_service.types.organization_conformance_pack_detailed_status

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.organization_conformance_pack_detailed_status.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationConformancePackDetailedStatuses:
    import capo_config_service.types.organization_conformance_pack_detailed_status

    out: OrganizationConformancePackDetailedStatuses = []
    for item in data:
        out.append(
            capo_config_service.types.organization_conformance_pack_detailed_status.deserialize_aws_json_1_1(
                item
            )
        )
    return out
