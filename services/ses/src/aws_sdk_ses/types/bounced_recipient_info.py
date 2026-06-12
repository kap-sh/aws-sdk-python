"""Generated from Smithy shape ``com.amazonaws.ses#BouncedRecipientInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ses.types.address
    import aws_sdk_ses.types.amazon_resource_name
    import aws_sdk_ses.types.bounce_type
    import aws_sdk_ses.types.recipient_dsn_fields


class BouncedRecipientInfo(TypedDict):
    recipient: "aws_sdk_ses.types.address.Address"
    """<p>The email address of the recipient of the bounced email.</p>"""
    recipient_arn: NotRequired[
        "aws_sdk_ses.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to receive email for the recipient of the bounced email. For more information about sending authorization, see the <a href=\"https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html\">Amazon SES Developer Guide</a>.</p>"""
    bounce_type: NotRequired["aws_sdk_ses.types.bounce_type.BounceType"]
    """<p>The reason for the bounce. You must provide either this parameter or <code>RecipientDsnFields</code>.</p>"""
    recipient_dsn_fields: NotRequired[
        "aws_sdk_ses.types.recipient_dsn_fields.RecipientDsnFields"
    ]
    """<p>Recipient-related DSN fields, most of which would normally be filled in automatically when provided with a <code>BounceType</code>. You must provide either this parameter or <code>BounceType</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: BouncedRecipientInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.Recipient", str(value["recipient"])))
    if "recipient_arn" in value:
        pairs.append((f"{prefix}.RecipientArn", str(value["recipient_arn"])))
    if "bounce_type" in value:
        import aws_sdk_ses.types.bounce_type

        aws_sdk_ses.types.bounce_type.serialize_query(
            value["bounce_type"], pairs, f"{prefix}.BounceType"
        )
    if "recipient_dsn_fields" in value:
        import aws_sdk_ses.types.recipient_dsn_fields

        aws_sdk_ses.types.recipient_dsn_fields.serialize_query(
            value["recipient_dsn_fields"], pairs, f"{prefix}.RecipientDsnFields"
        )


def deserialize_query(el: Element) -> BouncedRecipientInfo:
    out: BouncedRecipientInfo = {}  # type: ignore[typeddict-item]
    child_recipient = el.find("Recipient")
    if child_recipient is not None:
        out["recipient"] = str(child_recipient.text or "")
    else:
        raise DeserializationError("BouncedRecipientInfo.recipient required")
    child_recipient_arn = el.find("RecipientArn")
    if child_recipient_arn is not None:
        out["recipient_arn"] = str(child_recipient_arn.text or "")
    child_bounce_type = el.find("BounceType")
    if child_bounce_type is not None:
        import aws_sdk_ses.types.bounce_type

        out["bounce_type"] = aws_sdk_ses.types.bounce_type.deserialize_query(
            child_bounce_type
        )
    child_recipient_dsn_fields = el.find("RecipientDsnFields")
    if child_recipient_dsn_fields is not None:
        import aws_sdk_ses.types.recipient_dsn_fields

        out["recipient_dsn_fields"] = (
            aws_sdk_ses.types.recipient_dsn_fields.deserialize_query(
                child_recipient_dsn_fields
            )
        )
    return out
