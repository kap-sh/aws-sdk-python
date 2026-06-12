"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.provisioning_artifact_detail

ProvisioningArtifactDetails: TypeAlias = list[
    "aws_sdk_service_catalog.types.provisioning_artifact_detail.ProvisioningArtifactDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactDetails) -> list:
    import aws_sdk_service_catalog.types.provisioning_artifact_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.provisioning_artifact_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvisioningArtifactDetails:
    import aws_sdk_service_catalog.types.provisioning_artifact_detail

    out: ProvisioningArtifactDetails = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.provisioning_artifact_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out
