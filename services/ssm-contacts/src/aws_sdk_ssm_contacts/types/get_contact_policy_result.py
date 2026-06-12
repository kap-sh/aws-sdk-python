"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#GetContactPolicyResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.policy
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class GetContactPolicyResult(TypedDict):
    contact_arn: NotRequired[
        "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    ]
    """<p>The ARN of the contact or escalation plan.</p>"""
    policy: NotRequired["aws_sdk_ssm_contacts.types.policy.Policy"]
    """<p>Details about the resource policy attached to the contact or escalation plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContactPolicyResult) -> dict:
    out: dict = {}
    if "contact_arn" in value:
        out["ContactArn"] = value["contact_arn"]
    if "policy" in value:
        out["Policy"] = value["policy"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContactPolicyResult:
    out: GetContactPolicyResult = {}  # type: ignore[typeddict-item]
    if "ContactArn" in data:
        out["contact_arn"] = data["ContactArn"]
    if "Policy" in data:
        out["policy"] = data["Policy"]
    return out
