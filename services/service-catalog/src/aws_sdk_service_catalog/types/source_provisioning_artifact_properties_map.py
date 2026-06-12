"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SourceProvisioningArtifactPropertiesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.provisioning_artifact_property_name
    import aws_sdk_service_catalog.types.provisioning_artifact_property_value

SourceProvisioningArtifactPropertiesMap: TypeAlias = dict[
    "aws_sdk_service_catalog.types.provisioning_artifact_property_name.ProvisioningArtifactPropertyName",
    "aws_sdk_service_catalog.types.provisioning_artifact_property_value.ProvisioningArtifactPropertyValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: SourceProvisioningArtifactPropertiesMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_service_catalog.types.provisioning_artifact_property_name

        out[
            aws_sdk_service_catalog.types.provisioning_artifact_property_name.serialize_aws_json_1_1(
                key
            )
        ] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceProvisioningArtifactPropertiesMap:
    out: SourceProvisioningArtifactPropertiesMap = {}
    for key, value in data.items():
        import aws_sdk_service_catalog.types.provisioning_artifact_property_name

        out[
            aws_sdk_service_catalog.types.provisioning_artifact_property_name.deserialize_aws_json_1_1(
                key
            )
        ] = value
    return out
