"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.provisioning_artifact_parameter

ProvisioningArtifactParameters: TypeAlias = list[
    "capo_service_catalog.types.provisioning_artifact_parameter.ProvisioningArtifactParameter"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactParameters) -> list:
    import capo_service_catalog.types.provisioning_artifact_parameter

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioning_artifact_parameter.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvisioningArtifactParameters:
    import capo_service_catalog.types.provisioning_artifact_parameter

    out: ProvisioningArtifactParameters = []
    for item in data:
        out.append(
            capo_service_catalog.types.provisioning_artifact_parameter.deserialize_aws_json_1_1(
                item
            )
        )
    return out
