"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.provisioning_artifact_summary

ProvisioningArtifactSummaries: TypeAlias = list[
    "aws_sdk_service_catalog.types.provisioning_artifact_summary.ProvisioningArtifactSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactSummaries) -> list:
    import aws_sdk_service_catalog.types.provisioning_artifact_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_service_catalog.types.provisioning_artifact_summary.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvisioningArtifactSummaries:
    import aws_sdk_service_catalog.types.provisioning_artifact_summary

    out: ProvisioningArtifactSummaries = []
    for item in data:
        out.append(
            aws_sdk_service_catalog.types.provisioning_artifact_summary.deserialize_aws_json_1_1(
                item
            )
        )
    return out
