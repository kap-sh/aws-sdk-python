"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#GetContactPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class GetContactPolicyRequest(TypedDict):
    contact_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact or escalation plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContactPolicyRequest) -> dict:
    out: dict = {}
    out["ContactArn"] = value["contact_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContactPolicyRequest:
    out: GetContactPolicyRequest = {}  # type: ignore[typeddict-item]
    if "ContactArn" in data:
        out["contact_arn"] = data["ContactArn"]
    else:
        raise DeserializationError("GetContactPolicyRequest.contact_arn required")
    return out
