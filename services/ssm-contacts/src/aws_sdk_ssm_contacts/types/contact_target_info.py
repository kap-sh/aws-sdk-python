"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ContactTargetInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.is_essential
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class ContactTargetInfo(TypedDict, closed=True):
    contact_id: NotRequired[
        "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the contact.</p>"""
    is_essential: "aws_sdk_ssm_contacts.types.is_essential.IsEssential"
    """<p>A Boolean value determining if the contact's acknowledgement stops the progress of stages in the plan.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactTargetInfo) -> dict:
    out: dict = {}
    if "contact_id" in value:
        out["ContactId"] = value["contact_id"]
    out["IsEssential"] = value["is_essential"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ContactTargetInfo:
    out: ContactTargetInfo = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    if "IsEssential" in data:
        out["is_essential"] = data["IsEssential"]
    else:
        raise DeserializationError("ContactTargetInfo.is_essential required")
    return out
