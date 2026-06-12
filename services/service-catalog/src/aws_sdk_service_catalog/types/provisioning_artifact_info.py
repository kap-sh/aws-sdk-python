"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactInfo``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.provisioning_artifact_info_key
    import aws_sdk_service_catalog.types.provisioning_artifact_info_value

ProvisioningArtifactInfo: TypeAlias = dict[
    "aws_sdk_service_catalog.types.provisioning_artifact_info_key.ProvisioningArtifactInfoKey",
    "aws_sdk_service_catalog.types.provisioning_artifact_info_value.ProvisioningArtifactInfoValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: ProvisioningArtifactInfo) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisioningArtifactInfo:
    out: ProvisioningArtifactInfo = {}
    for key, value in data.items():
        out[key] = value
    return out
