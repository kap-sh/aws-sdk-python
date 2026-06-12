"""Generated from Smithy shape ``com.amazonaws.organizations#UpdatePolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_organizations.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_organizations.types.policy_content
    import aws_sdk_organizations.types.policy_description
    import aws_sdk_organizations.types.policy_id
    import aws_sdk_organizations.types.policy_name


class UpdatePolicyRequest(TypedDict):
    policy_id: "aws_sdk_organizations.types.policy_id.PolicyId"
    """<p>ID for the policy that you want to update.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> for a policy ID string requires \"p-\" followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).</p>"""
    name: NotRequired["aws_sdk_organizations.types.policy_name.PolicyName"]
    """<p>If provided, the new name for the policy.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> that is used to validate this parameter is a string of any of the characters in the ASCII character range.</p>"""
    description: NotRequired[
        "aws_sdk_organizations.types.policy_description.PolicyDescription"
    ]
    """<p>If provided, the new description for the policy.</p>"""
    content: NotRequired["aws_sdk_organizations.types.policy_content.PolicyContent"]
    """<p>If provided, the new content for the policy. The text must be correctly formatted JSON that complies with the syntax for the policy's type. For more information, see <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps_syntax.html\">SCP syntax</a> in the <i>Organizations User Guide</i>.</p> <p>The maximum size of a policy document depends on the policy's type. For more information, see <a href=\"https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html#min-max-values\">Maximum and minimum values</a> in the <i>Organizations User Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdatePolicyRequest) -> dict:
    out: dict = {}
    out["PolicyId"] = value["policy_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "content" in value:
        out["Content"] = value["content"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdatePolicyRequest:
    out: UpdatePolicyRequest = {}  # type: ignore[typeddict-item]
    if "PolicyId" in data:
        out["policy_id"] = data["PolicyId"]
    else:
        raise DeserializationError("UpdatePolicyRequest.policy_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Content" in data:
        out["content"] = data["Content"]
    return out
