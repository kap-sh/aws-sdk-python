"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateProvisioningArtifactOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_service_catalog.types.provisioning_artifact_detail
    import aws_sdk_service_catalog.types.provisioning_artifact_info
    import aws_sdk_service_catalog.types.status


class CreateProvisioningArtifactOutput(TypedDict, closed=True):
    provisioning_artifact_detail: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_detail.ProvisioningArtifactDetail"
    ]
    """<p>Information about the provisioning artifact.</p>"""
    info: NotRequired[
        "aws_sdk_service_catalog.types.provisioning_artifact_info.ProvisioningArtifactInfo"
    ]
    """<p>Specify the template source with one of the following options, but not both. Keys accepted: [ <code>LoadTemplateFromURL</code>, <code>ImportFromPhysicalId</code> ].</p> <p>Use the URL of the CloudFormation template in Amazon S3 or GitHub in JSON format. </p> <p> <code>LoadTemplateFromURL</code> </p> <p>Use the URL of the CloudFormation template in Amazon S3 or GitHub in JSON format.</p> <p> <code>ImportFromPhysicalId</code> </p> <p>Use the physical id of the resource that contains the template; currently supports CloudFormation stack ARN.</p>"""
    status: NotRequired["aws_sdk_service_catalog.types.status.Status"]
    """<p>The status of the current request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProvisioningArtifactOutput) -> dict:
    out: dict = {}
    if "provisioning_artifact_detail" in value:
        import aws_sdk_service_catalog.types.provisioning_artifact_detail

        out["ProvisioningArtifactDetail"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_detail.serialize_aws_json_1_1(
                value["provisioning_artifact_detail"]
            )
        )
    if "info" in value:
        import aws_sdk_service_catalog.types.provisioning_artifact_info

        out["Info"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_info.serialize_aws_json_1_1(
                value["info"]
            )
        )
    if "status" in value:
        import aws_sdk_service_catalog.types.status

        out["Status"] = aws_sdk_service_catalog.types.status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProvisioningArtifactOutput:
    out: CreateProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    if "ProvisioningArtifactDetail" in data:
        import aws_sdk_service_catalog.types.provisioning_artifact_detail

        out["provisioning_artifact_detail"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_detail.deserialize_aws_json_1_1(
                data["ProvisioningArtifactDetail"]
            )
        )
    if "Info" in data:
        import aws_sdk_service_catalog.types.provisioning_artifact_info

        out["info"] = (
            aws_sdk_service_catalog.types.provisioning_artifact_info.deserialize_aws_json_1_1(
                data["Info"]
            )
        )
    if "Status" in data:
        import aws_sdk_service_catalog.types.status

        out["status"] = aws_sdk_service_catalog.types.status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
