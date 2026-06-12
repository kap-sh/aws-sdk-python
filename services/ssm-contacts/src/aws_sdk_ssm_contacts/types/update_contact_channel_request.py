"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#UpdateContactChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.channel_name
    import aws_sdk_ssm_contacts.types.contact_channel_address
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class UpdateContactChannelRequest(TypedDict):
    contact_channel_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact channel you want to update.</p>"""
    name: NotRequired["aws_sdk_ssm_contacts.types.channel_name.ChannelName"]
    """<p>The name of the contact channel.</p>"""
    delivery_address: NotRequired[
        "aws_sdk_ssm_contacts.types.contact_channel_address.ContactChannelAddress"
    ]
    """<p>The details that Incident Manager uses when trying to engage the contact channel.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateContactChannelRequest) -> dict:
    out: dict = {}
    out["ContactChannelId"] = value["contact_channel_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "delivery_address" in value:
        import aws_sdk_ssm_contacts.types.contact_channel_address

        out["DeliveryAddress"] = (
            aws_sdk_ssm_contacts.types.contact_channel_address.serialize_aws_json_1_1(
                value["delivery_address"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateContactChannelRequest:
    out: UpdateContactChannelRequest = {}  # type: ignore[typeddict-item]
    if "ContactChannelId" in data:
        out["contact_channel_id"] = data["ContactChannelId"]
    else:
        raise DeserializationError(
            "UpdateContactChannelRequest.contact_channel_id required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    if "DeliveryAddress" in data:
        import aws_sdk_ssm_contacts.types.contact_channel_address

        out["delivery_address"] = (
            aws_sdk_ssm_contacts.types.contact_channel_address.deserialize_aws_json_1_1(
                data["DeliveryAddress"]
            )
        )
    return out
