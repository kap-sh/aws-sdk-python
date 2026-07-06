"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ContactChannel``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.activation_status
    import aws_sdk_ssm_contacts.types.channel_name
    import aws_sdk_ssm_contacts.types.channel_type
    import aws_sdk_ssm_contacts.types.contact_channel_address
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class ContactChannel(TypedDict, closed=True):
    contact_channel_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact channel.</p>"""
    contact_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the contact that contains the contact channel.</p>"""
    name: "aws_sdk_ssm_contacts.types.channel_name.ChannelName"
    """<p>The name of the contact channel.</p>"""
    type: NotRequired["aws_sdk_ssm_contacts.types.channel_type.ChannelType"]
    """<p>The type of the contact channel. Incident Manager supports three contact methods:</p> <ul> <li> <p>SMS</p> </li> <li> <p>VOICE</p> </li> <li> <p>EMAIL</p> </li> </ul>"""
    delivery_address: (
        "aws_sdk_ssm_contacts.types.contact_channel_address.ContactChannelAddress"
    )
    """<p>The details that Incident Manager uses when trying to engage the contact channel.</p>"""
    activation_status: "aws_sdk_ssm_contacts.types.activation_status.ActivationStatus"
    """<p>A Boolean value describing if the contact channel has been activated or not. If the contact channel isn't activated, Incident Manager can't engage the contact through it.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactChannel) -> dict:
    out: dict = {}
    out["ContactChannelArn"] = value["contact_channel_arn"]
    out["ContactArn"] = value["contact_arn"]
    out["Name"] = value["name"]
    if "type" in value:
        import aws_sdk_ssm_contacts.types.channel_type

        out["Type"] = aws_sdk_ssm_contacts.types.channel_type.serialize_aws_json_1_1(
            value["type"]
        )
    import aws_sdk_ssm_contacts.types.contact_channel_address

    out["DeliveryAddress"] = (
        aws_sdk_ssm_contacts.types.contact_channel_address.serialize_aws_json_1_1(
            value["delivery_address"]
        )
    )
    import aws_sdk_ssm_contacts.types.activation_status

    out["ActivationStatus"] = (
        aws_sdk_ssm_contacts.types.activation_status.serialize_aws_json_1_1(
            value["activation_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ContactChannel:
    out: ContactChannel = {}  # type: ignore[typeddict-item]
    if "ContactChannelArn" in data:
        out["contact_channel_arn"] = data["ContactChannelArn"]
    else:
        raise DeserializationError("ContactChannel.contact_channel_arn required")
    if "ContactArn" in data:
        out["contact_arn"] = data["ContactArn"]
    else:
        raise DeserializationError("ContactChannel.contact_arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ContactChannel.name required")
    if "Type" in data:
        import aws_sdk_ssm_contacts.types.channel_type

        out["type"] = aws_sdk_ssm_contacts.types.channel_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    if "DeliveryAddress" in data:
        import aws_sdk_ssm_contacts.types.contact_channel_address

        out["delivery_address"] = (
            aws_sdk_ssm_contacts.types.contact_channel_address.deserialize_aws_json_1_1(
                data["DeliveryAddress"]
            )
        )
    else:
        raise DeserializationError("ContactChannel.delivery_address required")
    if "ActivationStatus" in data:
        import aws_sdk_ssm_contacts.types.activation_status

        out["activation_status"] = (
            aws_sdk_ssm_contacts.types.activation_status.deserialize_aws_json_1_1(
                data["ActivationStatus"]
            )
        )
    else:
        raise DeserializationError("ContactChannel.activation_status required")
    return out
