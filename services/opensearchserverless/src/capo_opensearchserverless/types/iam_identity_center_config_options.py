"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IamIdentityCenterConfigOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.iam_identity_center_application_arn
    import capo_opensearchserverless.types.iam_identity_center_group_attribute
    import capo_opensearchserverless.types.iam_identity_center_instance_arn
    import capo_opensearchserverless.types.iam_identity_center_user_attribute


class IamIdentityCenterConfigOptions(TypedDict, closed=True):
    instance_arn: NotRequired[
        "capo_opensearchserverless.types.iam_identity_center_instance_arn.IamIdentityCenterInstanceArn"
    ]
    """<p>The ARN of the IAM Identity Center instance used to integrate with OpenSearch Serverless.</p>"""
    application_arn: NotRequired[
        "capo_opensearchserverless.types.iam_identity_center_application_arn.IamIdentityCenterApplicationArn"
    ]
    """<p>The ARN of the IAM Identity Center application used to integrate with OpenSearch Serverless.</p>"""
    application_name: NotRequired["str"]
    """<p>The name of the IAM Identity Center application used to integrate with OpenSearch Serverless.</p>"""
    application_description: NotRequired["str"]
    """<p>The description of the IAM Identity Center application used to integrate with OpenSearch Serverless.</p>"""
    user_attribute: NotRequired[
        "capo_opensearchserverless.types.iam_identity_center_user_attribute.IamIdentityCenterUserAttribute"
    ]
    """<p>The user attribute for this IAM Identity Center integration. Defaults to <code>UserId</code> </p>"""
    group_attribute: NotRequired[
        "capo_opensearchserverless.types.iam_identity_center_group_attribute.IamIdentityCenterGroupAttribute"
    ]
    """<p>The group attribute for this IAM Identity Center integration. Defaults to <code>GroupId</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IamIdentityCenterConfigOptions) -> dict:
    out: dict = {}
    if "instance_arn" in value:
        out["instanceArn"] = value["instance_arn"]
    if "application_arn" in value:
        out["applicationArn"] = value["application_arn"]
    if "application_name" in value:
        out["applicationName"] = value["application_name"]
    if "application_description" in value:
        out["applicationDescription"] = value["application_description"]
    if "user_attribute" in value:
        out["userAttribute"] = value["user_attribute"]
    if "group_attribute" in value:
        out["groupAttribute"] = value["group_attribute"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IamIdentityCenterConfigOptions:
    out: IamIdentityCenterConfigOptions = {}  # type: ignore[typeddict-item]
    if "instanceArn" in data:
        out["instance_arn"] = data["instanceArn"]
    if "applicationArn" in data:
        out["application_arn"] = data["applicationArn"]
    if "applicationName" in data:
        out["application_name"] = data["applicationName"]
    if "applicationDescription" in data:
        out["application_description"] = data["applicationDescription"]
    if "userAttribute" in data:
        out["user_attribute"] = data["userAttribute"]
    if "groupAttribute" in data:
        out["group_attribute"] = data["groupAttribute"]
    return out
