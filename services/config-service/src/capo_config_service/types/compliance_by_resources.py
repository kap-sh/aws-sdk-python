"""Generated from Smithy shape ``com.amazonaws.configservice#ComplianceByResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_config_service.types.compliance_by_resource

ComplianceByResources: TypeAlias = list[
    "capo_config_service.types.compliance_by_resource.ComplianceByResource"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ComplianceByResources) -> list:
    import capo_config_service.types.compliance_by_resource

    out: list = []
    for item in value:
        out.append(
            capo_config_service.types.compliance_by_resource.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ComplianceByResources:
    import capo_config_service.types.compliance_by_resource

    out: ComplianceByResources = []
    for item in data:
        out.append(
            capo_config_service.types.compliance_by_resource.deserialize_aws_json_1_1(
                item
            )
        )
    return out
