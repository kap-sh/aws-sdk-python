"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.output_description
    import aws_sdk_service_catalog.types.provisioning_artifact_output_key


class ProvisioningArtifactOutput(TypedDict):
    key: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_output_key.ProvisioningArtifactOutputKey"
    ]
    """<p>The provisioning artifact output key.</p>"""
    description: NotRequired[
        "aws_sdk_service_catalog.types.output_description.OutputDescription"
    ]
    """<p>Description of the provisioning artifact output key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactOutput) -> dict:
    out: dict = {}
    if "key" in value:
        out["Key"] = value["key"]
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisioningArtifactOutput:
    out: ProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        out["key"] = data["Key"]
    if "Description" in data:
        out["description"] = data["Description"]
    return out
