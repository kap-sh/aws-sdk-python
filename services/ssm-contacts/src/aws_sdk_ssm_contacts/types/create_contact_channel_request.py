"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#CreateContactChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.channel_name
    import aws_sdk_ssm_contacts.types.channel_type
    import aws_sdk_ssm_contacts.types.contact_channel_address
    import aws_sdk_ssm_contacts.types.defer_activation
    import aws_sdk_ssm_contacts.types.idempotency_token
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class CreateContactChannelRequest(TypedDict):
    contact_id: "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    """<p>The Amazon Resource Name (ARN) of the contact you are adding the contact channel to.</p>"""
    name: "aws_sdk_ssm_contacts.types.channel_name.ChannelName"
    """<p>The name of the contact channel.</p>"""
    type: "aws_sdk_ssm_contacts.types.channel_type.ChannelType"
    """<p>Incident Manager supports three types of contact channels:</p> <ul> <li> <p> <code>SMS</code> </p> </li> <li> <p> <code>VOICE</code> </p> </li> <li> <p> <code>EMAIL</code> </p> </li> </ul>"""
    delivery_address: (
        "aws_sdk_ssm_contacts.types.contact_channel_address.ContactChannelAddress"
    )
    """<p>The details that Incident Manager uses when trying to engage the contact channel. The format is dependent on the type of the contact channel. The following are the expected formats:</p> <ul> <li> <p>SMS - '+' followed by the country code and phone number</p> </li> <li> <p>VOICE - '+' followed by the country code and phone number</p> </li> <li> <p>EMAIL - any standard email format</p> </li> </ul>"""
    defer_activation: NotRequired[
        "aws_sdk_ssm_contacts.types.defer_activation.DeferActivation"
    ]
    """<p>If you want to activate the channel at a later time, you can choose to defer activation. Incident Manager can't engage your contact channel until it has been activated.</p>"""
    idempotency_token: NotRequired[
        "aws_sdk_ssm_contacts.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A token ensuring that the operation is called only once with the specified details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateContactChannelRequest) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
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
    if "defer_activation" in value:
        out["DeferActivation"] = value["defer_activation"]
    if "idempotency_token" in value:
        out["IdempotencyToken"] = value["idempotency_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateContactChannelRequest:
    out: CreateContactChannelRequest = {}  # type: ignore[typeddict-item]
    if "ContactId" in data:
        out["contact_id"] = data["ContactId"]
    else:
        raise DeserializationError("CreateContactChannelRequest.contact_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("CreateContactChannelRequest.name required")
    if "Type" in data:
        import aws_sdk_ssm_contacts.types.channel_type

        out["type"] = aws_sdk_ssm_contacts.types.channel_type.deserialize_aws_json_1_1(
            data["Type"]
        )
    else:
        raise DeserializationError("CreateContactChannelRequest.type required")
    if "DeliveryAddress" in data:
        import aws_sdk_ssm_contacts.types.contact_channel_address

        out["delivery_address"] = (
            aws_sdk_ssm_contacts.types.contact_channel_address.deserialize_aws_json_1_1(
                data["DeliveryAddress"]
            )
        )
    else:
        raise DeserializationError(
            "CreateContactChannelRequest.delivery_address required"
        )
    if "DeferActivation" in data:
        out["defer_activation"] = data["DeferActivation"]
    if "IdempotencyToken" in data:
        out["idempotency_token"] = data["IdempotencyToken"]
    return out
