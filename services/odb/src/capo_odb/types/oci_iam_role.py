"""Generated from Smithy shape ``com.amazonaws.odb#OciIamRole``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.oci_aws_integration
    import capo_odb.types.role_arn


class OciIamRole(TypedDict, closed=True):
    iam_role_arn: NotRequired["capo_odb.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) service role.</p>"""
    aws_integration: NotRequired["capo_odb.types.oci_aws_integration.OciAwsIntegration"]
    """<p>The Amazon Web Services integration configuration settings for the Amazon Web Services Identity and Access Management (IAM) service role.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OciIamRole) -> dict:
    out: dict = {}
    if "iam_role_arn" in value:
        out["iamRoleArn"] = value["iam_role_arn"]
    if "aws_integration" in value:
        import capo_odb.types.oci_aws_integration

        out["awsIntegration"] = (
            capo_odb.types.oci_aws_integration.serialize_aws_json_1_0(
                value["aws_integration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> OciIamRole:
    out: OciIamRole = {}  # type: ignore[typeddict-item]
    if "iamRoleArn" in data:
        out["iam_role_arn"] = data["iamRoleArn"]
    if "awsIntegration" in data:
        import capo_odb.types.oci_aws_integration

        out["aws_integration"] = (
            capo_odb.types.oci_aws_integration.deserialize_aws_json_1_0(
                data["awsIntegration"]
            )
        )
    return out
