"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#GetContactRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class GetContactRequest(TypedDict, closed=True):
    contact_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact or escalation plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContactRequest) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContactRequest:
    out: GetContactRequest = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("GetContactRequest.contact_id required")
    return out
