"""Generated from Smithy shape ``com.amazonaws.odb#AssociateIamRoleToResourceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_odb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.arn
    import aws_sdk_odb.types.role_arn
    import aws_sdk_odb.types.supported_aws_integration


class AssociateIamRoleToResourceInput(TypedDict, closed=True):
    iam_role_arn: "aws_sdk_odb.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Identity and Access Management (IAM) service role to associate with the resource.</p>"""
    aws_integration: (
        "aws_sdk_odb.types.supported_aws_integration.SupportedAwsIntegration"
    )
    """<p>The Amazon Web Services integration configuration settings for the Amazon Web Services Identity and Access Management (IAM) service role association.</p>"""
    resource_arn: "aws_sdk_odb.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the target resource to associate with the Amazon Web Services Identity and Access Management (IAM) service role.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateIamRoleToResourceInput) -> dict:
    out: dict = {}
    out["iamRoleArn"] = value["iam_role_arn"]
    import aws_sdk_odb.types.supported_aws_integration

    out["awsIntegration"] = (
        aws_sdk_odb.types.supported_aws_integration.serialize_aws_json_1_0(
            value["aws_integration"]
        )
    )
    out["resourceArn"] = value["resource_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateIamRoleToResourceInput:
    out: AssociateIamRoleToResourceInput = {}  # type: ignore[typeddict-item]
    if "iamRoleArn" in data:
        out["iam_role_arn"] = data["iamRoleArn"]
    else:
        raise DeserializationError(
            "AssociateIamRoleToResourceInput.iam_role_arn required"
        )
    if "awsIntegration" in data:
        import aws_sdk_odb.types.supported_aws_integration

        out["aws_integration"] = (
            aws_sdk_odb.types.supported_aws_integration.deserialize_aws_json_1_0(
                data["awsIntegration"]
            )
        )
    else:
        raise DeserializationError(
            "AssociateIamRoleToResourceInput.aws_integration required"
        )
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError(
            "AssociateIamRoleToResourceInput.resource_arn required"
        )
    return out
