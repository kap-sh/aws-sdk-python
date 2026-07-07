"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#GetContactChannelResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.activation_status
    import aws_sdk_ssm_contacts.types.channel_name
    import aws_sdk_ssm_contacts.types.channel_type
    import aws_sdk_ssm_contacts.types.contact_channel_address
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class GetContactChannelResult(TypedDict, closed=True):
    contact_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the contact that the channel belongs to.</p>"""
    contact_channel_arn: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The ARN of the contact channel.</p>"""
    name: "aws_sdk_ssm_contacts.types.channel_name.ChannelName"
    """<p>The name of the contact channel</p>"""
    type: "aws_sdk_ssm_contacts.types.channel_type.ChannelType"
    """<p>The type of contact channel. The type is <code>SMS</code>, <code>VOICE</code>, or <code>EMAIL</code>.</p>"""
    delivery_address: (
        "aws_sdk_ssm_contacts.types.contact_channel_address.ContactChannelAddress"
    )
    """<p>The details that Incident Manager uses when trying to engage the contact channel.</p>"""
    activation_status: NotRequired[
        "aws_sdk_ssm_contacts.types.activation_status.ActivationStatus"
    ]
    """<p>A Boolean value indicating if the contact channel has been activated or not.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetContactChannelResult) -> dict:
    out: dict = {}
    out["ContactArn"] = value["contact_arn"]
    out["ContactChannelArn"] = value["contact_channel_arn"]
    out["Name"] = value["name"]
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
    if "activation_status" in value:
        import aws_sdk_ssm_contacts.types.activation_status

        out["ActivationStatus"] = (
            aws_sdk_ssm_contacts.types.activation_status.serialize_aws_json_1_1(
                value["activation_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetContactChannelResult:
    out: GetContactChannelResult = {}  # type: ignore[typeddict-item]
    if "ContactArn" in data:
        out["contact_arn"] = data["ContactArn"]
    else:
        raise DeserializationError("GetContactChannelResult.contact_arn required")
    if "ContactChannelArn" in data:
        out["contact_channel_arn"] = data["ContactChannelArn"]
    else:
        raise DeserializationError(
            "GetContactChannelResult.contact_channel_arn required"
        )
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GetContactChannelResult.name required")
    if "Type" in data:
        import aws_sdk_ssm_contacts.types.channel_type

        out["type"] = aws_sdk_ssm_contacts.types.channel_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("GetContactChannelResult.type required")
    if "DeliveryAddress" in data:
        import aws_sdk_ssm_contacts.types.contact_channel_address

        out["delivery_address"] = (
            aws_sdk_ssm_contacts.types.contact_channel_address.deserialize_aws_json_1_1(
                data["DeliveryAddress"]
            )
        )
    else:
        raise DeserializationError("GetContactChannelResult.delivery_address required")
    if "ActivationStatus" in data:
        import aws_sdk_ssm_contacts.types.activation_status

        out["activation_status"] = (
            aws_sdk_ssm_contacts.types.activation_status.deserialize_aws_json_1_1(
                data["ActivationStatus"]
            )
        )
    return out
