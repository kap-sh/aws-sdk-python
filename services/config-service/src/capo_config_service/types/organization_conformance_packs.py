"""Generated from Smithy shape ``com.amazonaws.configservice#OrganizationConformancePacks``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.organization_conformance_pack

OrganizationConformancePacks: TypeAlias = list[
    "capo_config_service.types.organization_conformance_pack.OrganizationConformancePack"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrganizationConformancePacks) -> list:
    import capo_config_service.types.organization_conformance_pack

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.organization_conformance_pack.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> OrganizationConformancePacks:
    import capo_config_service.types.organization_conformance_pack

    out: OrganizationConformancePacks = []
    for item in data:
        out.append(
            capo_config_service.types.organization_conformance_pack.deserialize_aws_json_1_1(
                item
            )
        )
    return out
