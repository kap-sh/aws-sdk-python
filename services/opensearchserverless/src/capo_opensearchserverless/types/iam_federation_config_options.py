"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#IamFederationConfigOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.iam_federation_group_attribute
    import capo_opensearchserverless.types.iam_federation_user_attribute


class IamFederationConfigOptions(TypedDict, closed=True):
    group_attribute: NotRequired[
        "capo_opensearchserverless.types.iam_federation_group_attribute.iamFederationGroupAttribute"
    ]
    """<p>The group attribute for this IAM federation integration. This attribute is used to map identity provider groups to OpenSearch Serverless permissions.</p>"""
    user_attribute: NotRequired[
        "capo_opensearchserverless.types.iam_federation_user_attribute.iamFederationUserAttribute"
    ]
    """<p>The user attribute for this IAM federation integration. This attribute is used to identify users in the federated authentication process.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IamFederationConfigOptions) -> dict:
    out: dict = {}
    if "group_attribute" in value:
        out["groupAttribute"] = value["group_attribute"]
    if "user_attribute" in value:
        out["userAttribute"] = value["user_attribute"]
    return out


def deserialize_aws_json_1_0(data: dict) -> IamFederationConfigOptions:
    out: IamFederationConfigOptions = {}  # type: ignore[typeddict-item]
    if "groupAttribute" in data:
        out["group_attribute"] = data["groupAttribute"]
    if "userAttribute" in data:
        out["user_attribute"] = data["userAttribute"]
    return out
