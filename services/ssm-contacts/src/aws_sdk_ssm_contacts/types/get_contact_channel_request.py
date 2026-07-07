"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#GetContactChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class GetContactChannelRequest(TypedDict, closed=True):
    contact_channel_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact channel you want information about.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContactChannelRequest) -> dict:
    out: dict = {}
    out["ContactChannelId"] = value["contact_channel_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContactChannelRequest:
    out: GetContactChannelRequest = {}  # type: ignore[typeddict-item]
    if "ContactChannelId" in data:
        out["contact_channel_id"] = data["ContactChannelId"]
    else:
        raise DeserializationError(
            "GetContactChannelRequest.contact_channel_id required"
        )
    return out
