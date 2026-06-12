"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.provisioning_artifact

ProvisioningArtifacts: TypeAlias = list[
    "aws_sdk_service_catalog.types.provisioning_artifact.ProvisioningArtifact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifacts) -> list:
    import aws_sdk_service_catalog.types.provisioning_artifact

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.provisioning_artifact.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvisioningArtifacts:
    import aws_sdk_service_catalog.types.provisioning_artifact

    out: ProvisioningArtifacts = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.provisioning_artifact.deserialize_aws_json_1_1(
                item
            )
        )
    return out
