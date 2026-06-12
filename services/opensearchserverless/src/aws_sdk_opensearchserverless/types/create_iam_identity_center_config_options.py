"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CreateIamIdentityCenterConfigOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_opensearchserverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.iam_identity_center_group_attribute
    import aws_sdk_opensearchserverless.types.iam_identity_center_instance_arn
    import aws_sdk_opensearchserverless.types.iam_identity_center_user_attribute


class CreateIamIdentityCenterConfigOptions(TypedDict):
    instance_arn: "aws_sdk_opensearchserverless.types.iam_identity_center_instance_arn.IamIdentityCenterInstanceArn"
    """<p>The ARN of the IAM Identity Center instance used to integrate with OpenSearch Serverless.</p>"""
    user_attribute: NotRequired[
        "aws_sdk_opensearchserverless.types.iam_identity_center_user_attribute.IamIdentityCenterUserAttribute"
    ]
    """<p>The user attribute for this IAM Identity Center integration. Defaults to <code>UserId</code>.</p>"""
    group_attribute: NotRequired[
        "aws_sdk_opensearchserverless.types.iam_identity_center_group_attribute.IamIdentityCenterGroupAttribute"
    ]
    """<p>The group attribute for this IAM Identity Center integration. Defaults to <code>GroupId</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateIamIdentityCenterConfigOptions) -> dict:
    out: dict = {}
    out["instanceArn"] = value["instance_arn"]
    if "user_attribute" in value:
        out["userAttribute"] = value["user_attribute"]
    if "group_attribute" in value:
        out["groupAttribute"] = value["group_attribute"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateIamIdentityCenterConfigOptions:
    out: CreateIamIdentityCenterConfigOptions = {}  # type: ignore[typeddict-item]
    if "instanceArn" in data:
        out["instance_arn"] = data["instanceArn"]
    else:
        raise DeserializationError(
            "CreateIamIdentityCenterConfigOptions.instance_arn required"
        )
    if "userAttribute" in data:
        out["user_attribute"] = data["userAttribute"]
    if "groupAttribute" in data:
        out["group_attribute"] = data["groupAttribute"]
    return out
