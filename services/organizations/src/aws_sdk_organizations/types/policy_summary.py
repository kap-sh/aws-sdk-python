"""Generated from Smithy shape ``com.amazonaws.organizations#PolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_organizations.types.aws_managed_policy
    import aws_sdk_organizations.types.policy_arn
    import aws_sdk_organizations.types.policy_description
    import aws_sdk_organizations.types.policy_id
    import aws_sdk_organizations.types.policy_name
    import aws_sdk_organizations.types.policy_type


class PolicySummary(TypedDict, closed=True):
    id: NotRequired["aws_sdk_organizations.types.policy_id.PolicyId"]
    r"""<p>The unique identifier (ID) of the policy.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> for a policy ID string requires \"p-\" followed by from 8 to 128 lowercase or uppercase letters, digits, or the underscore character (_).</p>"""
    arn: NotRequired["aws_sdk_organizations.types.policy_arn.PolicyArn"]
    r"""<p>The Amazon Resource Name (ARN) of the policy.</p> <p>For more information about ARNs in Organizations, see <a href=\"https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsorganizations.html#awsorganizations-resources-for-iam-policies\">ARN Formats Supported by Organizations</a> in the <i>Amazon Web Services Service Authorization Reference</i>.</p>"""
    name: NotRequired["aws_sdk_organizations.types.policy_name.PolicyName"]
    r"""<p>The friendly name of the policy.</p> <p>The <a href=\"http://wikipedia.org/wiki/regex\">regex pattern</a> that is used to validate this parameter is a string of any of the characters in the ASCII character range.</p>"""
    description: NotRequired[
        "aws_sdk_organizations.types.policy_description.PolicyDescription"
    ]
    """<p>The description of the policy.</p>"""
    type: NotRequired["aws_sdk_organizations.types.policy_type.PolicyType"]
    """<p>The type of policy.</p>"""
    aws_managed: "aws_sdk_organizations.types.aws_managed_policy.AwsManagedPolicy"
    """<p>A boolean value that indicates whether the specified policy is an Amazon Web Services managed policy. If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicySummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import aws_sdk_organizations.types.policy_type

        out["Type"] = aws_sdk_organizations.types.policy_type.serialize_aws_json_1_1(
            value["type"]
        )
    out["AwsManaged"] = value.get("aws_managed", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicySummary:
    out: PolicySummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        import aws_sdk_organizations.types.policy_type

        out["type"] = aws_sdk_organizations.types.policy_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "AwsManaged" in data:
        out["aws_managed"] = data["AwsManaged"]
    else:
        out["aws_managed"] = False
    return out
