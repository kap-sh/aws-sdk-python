"""Generated from Smithy shape ``com.amazonaws.connect#SendOutboundEmailRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.client_token
    import aws_sdk_connect.types.email_address_info
    import aws_sdk_connect.types.instance_id
    import aws_sdk_connect.types.outbound_additional_recipients
    import aws_sdk_connect.types.outbound_email_content
    import aws_sdk_connect.types.source_campaign
    import aws_sdk_connect.types.traffic_type


class SendOutboundEmailRequest(TypedDict, closed=True):
    instance_id: "aws_sdk_connect.types.instance_id.InstanceId"
    r"""<p>The identifier of the Connect Customer instance. You can <a href=\"https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html\">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    from_email_address: "aws_sdk_connect.types.email_address_info.EmailAddressInfo"
    """<p>The email address to be used for sending email.</p>"""
    destination_email_address: (
        "aws_sdk_connect.types.email_address_info.EmailAddressInfo"
    )
    """<p>The email address to send the email to.</p>"""
    additional_recipients: NotRequired[
        "aws_sdk_connect.types.outbound_additional_recipients.OutboundAdditionalRecipients"
    ]
    """<p>The additional recipients address of the email in CC.</p>"""
    email_message: "aws_sdk_connect.types.outbound_email_content.OutboundEmailContent"
    """<p>The email message body to be sent to the newly created email.</p>"""
    traffic_type: "aws_sdk_connect.types.traffic_type.TrafficType"
    """<p>Denotes the class of traffic.</p> <note> <p>Only the CAMPAIGN traffic type is supported.</p> </note>"""
    source_campaign: NotRequired["aws_sdk_connect.types.source_campaign.SourceCampaign"]
    """<p>A Campaign object need for Campaign traffic type.</p>"""
    client_token: NotRequired["aws_sdk_connect.types.client_token.ClientToken"]
    r"""<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href=\"https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/\">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendOutboundEmailRequest) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.email_address_info

    out["FromEmailAddress"] = aws_sdk_connect.types.email_address_info.serialize_json(
        value["from_email_address"]
    )
    import aws_sdk_connect.types.email_address_info

    out["DestinationEmailAddress"] = (
        aws_sdk_connect.types.email_address_info.serialize_json(
            value["destination_email_address"]
        )
    )
    if "additional_recipients" in value:
        import aws_sdk_connect.types.outbound_additional_recipients

        out["AdditionalRecipients"] = (
            aws_sdk_connect.types.outbound_additional_recipients.serialize_json(
                value["additional_recipients"]
            )
        )
    import aws_sdk_connect.types.outbound_email_content

    out["EmailMessage"] = aws_sdk_connect.types.outbound_email_content.serialize_json(
        value["email_message"]
    )
    import aws_sdk_connect.types.traffic_type

    out["TrafficType"] = aws_sdk_connect.types.traffic_type.serialize_json(
        value["traffic_type"]
    )
    if "source_campaign" in value:
        import aws_sdk_connect.types.source_campaign

        out["SourceCampaign"] = aws_sdk_connect.types.source_campaign.serialize_json(
            value["source_campaign"]
        )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> SendOutboundEmailRequest:
    out: SendOutboundEmailRequest = {}  # type: ignore[typeddict-item]
    if "FromEmailAddress" in data:
        import aws_sdk_connect.types.email_address_info

        out["from_email_address"] = (
            aws_sdk_connect.types.email_address_info.deserialize_json(
                data["FromEmailAddress"]
            )
        )
    else:
        raise DeserializationError(
            "SendOutboundEmailRequest.from_email_address required"
        )
    if "DestinationEmailAddress" in data:
        import aws_sdk_connect.types.email_address_info

        out["destination_email_address"] = (
            aws_sdk_connect.types.email_address_info.deserialize_json(
                data["DestinationEmailAddress"]
            )
        )
    else:
        raise DeserializationError(
            "SendOutboundEmailRequest.destination_email_address required"
        )
    if "AdditionalRecipients" in data:
        import aws_sdk_connect.types.outbound_additional_recipients

        out["additional_recipients"] = (
            aws_sdk_connect.types.outbound_additional_recipients.deserialize_json(
                data["AdditionalRecipients"]
            )
        )
    if "EmailMessage" in data:
        import aws_sdk_connect.types.outbound_email_content

        out["email_message"] = (
            aws_sdk_connect.types.outbound_email_content.deserialize_json(
                data["EmailMessage"]
            )
        )
    else:
        raise DeserializationError("SendOutboundEmailRequest.email_message required")
    if "TrafficType" in data:
        import aws_sdk_connect.types.traffic_type

        out["traffic_type"] = aws_sdk_connect.types.traffic_type.deserialize_json(
            data["TrafficType"]
        )
    else:
        raise DeserializationError("SendOutboundEmailRequest.traffic_type required")
    if "SourceCampaign" in data:
        import aws_sdk_connect.types.source_campaign

        out["source_campaign"] = aws_sdk_connect.types.source_campaign.deserialize_json(
            data["SourceCampaign"]
        )
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    return out
