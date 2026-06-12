"""Generated from Smithy shape ``com.amazonaws.ssm#PatchStatus``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.date_time
    import aws_sdk_ssm.types.patch_compliance_level
    import aws_sdk_ssm.types.patch_deployment_status


class PatchStatus(TypedDict):
    deployment_status: NotRequired[
        "aws_sdk_ssm.types.patch_deployment_status.PatchDeploymentStatus"
    ]
    """<p>The approval status of a patch.</p>"""
    compliance_level: NotRequired[
        "aws_sdk_ssm.types.patch_compliance_level.PatchComplianceLevel"
    ]
    """<p>The compliance severity level for a patch.</p>"""
    approval_date: NotRequired["aws_sdk_ssm.types.date_time.DateTime"]
    """<p>The date the patch was approved (or will be approved if the status is <code>PENDING_APPROVAL</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchStatus) -> dict:
    out: dict = {}
    if "deployment_status" in value:
        import aws_sdk_ssm.types.patch_deployment_status

        out["DeploymentStatus"] = (
            aws_sdk_ssm.types.patch_deployment_status.serialize_aws_json_1_1(
                value["deployment_status"]
            )
        )
    if "compliance_level" in value:
        import aws_sdk_ssm.types.patch_compliance_level

        out["ComplianceLevel"] = (
            aws_sdk_ssm.types.patch_compliance_level.serialize_aws_json_1_1(
                value["compliance_level"]
            )
        )
    if "approval_date" in value:
        import aws_sdk_ssm.types.date_time

        out["ApprovalDate"] = aws_sdk_ssm.types.date_time.serialize_aws_json_1_1(
            value["approval_date"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PatchStatus:
    out: PatchStatus = {}  # type: ignore[typeddict-item]
    if "DeploymentStatus" in data:
        import aws_sdk_ssm.types.patch_deployment_status

        out["deployment_status"] = (
            aws_sdk_ssm.types.patch_deployment_status.deserialize_aws_json_1_1(
                data["DeploymentStatus"]
            )
        )
    if "ComplianceLevel" in data:
        import aws_sdk_ssm.types.patch_compliance_level

        out["compliance_level"] = (
            aws_sdk_ssm.types.patch_compliance_level.deserialize_aws_json_1_1(
                data["ComplianceLevel"]
            )
        )
    if "ApprovalDate" in data:
        import aws_sdk_ssm.types.date_time

        out["approval_date"] = aws_sdk_ssm.types.date_time.deserialize_aws_json_1_1(
            data["ApprovalDate"]
        )
    return out
