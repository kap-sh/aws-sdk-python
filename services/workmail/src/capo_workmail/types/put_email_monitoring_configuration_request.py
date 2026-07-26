"""Generated from Smithy shape ``com.amazonaws.workmail#PutEmailMonitoringConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workmail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workmail.types.log_group_arn
    import capo_workmail.types.organization_id
    import capo_workmail.types.role_arn


class PutEmailMonitoringConfigurationRequest(TypedDict, closed=True):
    organization_id: "capo_workmail.types.organization_id.OrganizationId"
    """<p>The ID of the organization for which the email monitoring configuration is set.</p>"""
    role_arn: NotRequired["capo_workmail.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM Role associated with the email monitoring configuration. If absent, the IAM Role Arn of AWSServiceRoleForAmazonWorkMailEvents will be used.</p>"""
    log_group_arn: "capo_workmail.types.log_group_arn.LogGroupArn"
    """<p>The Amazon Resource Name (ARN) of the CloudWatch Log group associated with the email monitoring configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutEmailMonitoringConfigurationRequest) -> dict:
    out: dict = {}
    out["OrganizationId"] = value["organization_id"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    out["LogGroupArn"] = value["log_group_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutEmailMonitoringConfigurationRequest:
    out: PutEmailMonitoringConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "OrganizationId" in data:
        out["organization_id"] = data["OrganizationId"]
    else:
        raise DeserializationError(
            "PutEmailMonitoringConfigurationRequest.organization_id required"
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "LogGroupArn" in data:
        out["log_group_arn"] = data["LogGroupArn"]
    else:
        raise DeserializationError(
            "PutEmailMonitoringConfigurationRequest.log_group_arn required"
        )
    return out
