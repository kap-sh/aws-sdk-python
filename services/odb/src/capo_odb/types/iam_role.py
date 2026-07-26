"""Generated from Smithy shape ``com.amazonaws.odb#IamRole``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.iam_role_status
    import capo_odb.types.role_arn
    import capo_odb.types.supported_aws_integration


class IamRole(TypedDict, closed=True):
    iam_role_arn: NotRequired["capo_odb.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) service role.</p>"""
    status: NotRequired["capo_odb.types.iam_role_status.IamRoleStatus"]
    """<p>The current status of the Amazon Web Services Identity and Access Management (IAM) service role.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the Amazon Web Services Identity and Access Management (IAM) service role, if applicable.</p>"""
    aws_integration: NotRequired[
        "capo_odb.types.supported_aws_integration.SupportedAwsIntegration"
    ]
    """<p>The Amazon Web Services integration configuration settings for the Amazon Web Services Identity and Access Management (IAM) service role.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IamRole) -> dict:
    out: dict = {}
    if "iam_role_arn" in value:
        out["iamRoleArn"] = value["iam_role_arn"]
    if "status" in value:
        import capo_odb.types.iam_role_status

        out["status"] = capo_odb.types.iam_role_status.serialize_aws_json_1_0(
            value["status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "aws_integration" in value:
        import capo_odb.types.supported_aws_integration

        out["awsIntegration"] = (
            capo_odb.types.supported_aws_integration.serialize_aws_json_1_0(
                value["aws_integration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IamRole:
    out: IamRole = {}  # type: ignore[typeddict-item]
    if "iamRoleArn" in data:
        out["iam_role_arn"] = data["iamRoleArn"]
    if "status" in data:
        import capo_odb.types.iam_role_status

        out["status"] = capo_odb.types.iam_role_status.deserialize_aws_json_1_0(
            data["status"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "awsIntegration" in data:
        import capo_odb.types.supported_aws_integration

        out["aws_integration"] = (
            capo_odb.types.supported_aws_integration.deserialize_aws_json_1_0(
                data["awsIntegration"]
            )
        )
    return out
