"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#Receipt``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_contacts.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.date_time
    import aws_sdk_ssm_contacts.types.receipt_info
    import aws_sdk_ssm_contacts.types.receipt_type
    import aws_sdk_ssm_contacts.types.ssm_contacts_arn


class Receipt(TypedDict):
    contact_channel_arn: NotRequired[
        "aws_sdk_ssm_contacts.types.ssm_contacts_arn.SsmContactsArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the contact channel Incident Manager engaged.</p>"""
    receipt_type: "aws_sdk_ssm_contacts.types.receipt_type.ReceiptType"
    """<p>The type follows the engagement cycle, <code>SENT</code>, <code>DELIVERED</code>, and <code>READ</code>.</p>"""
    receipt_info: NotRequired["aws_sdk_ssm_contacts.types.receipt_info.ReceiptInfo"]
    """<p>Information provided during the page acknowledgement.</p>"""
    receipt_time: "aws_sdk_ssm_contacts.types.date_time.DateTime"
    """<p>The time receipt was <code>SENT</code>, <code>DELIVERED</code>, or <code>READ</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Receipt) -> dict:
    out: dict = {}
    if "contact_channel_arn" in value:
        out["ContactChannelArn"] = value["contact_channel_arn"]
    import aws_sdk_ssm_contacts.types.receipt_type

    out["ReceiptType"] = aws_sdk_ssm_contacts.types.receipt_type.serialize_aws_json_1_1(
        value["receipt_type"]
    )
    if "receipt_info" in value:
        out["ReceiptInfo"] = value["receipt_info"]
    import aws_sdk_ssm_contacts.types.date_time

    out["ReceiptTime"] = aws_sdk_ssm_contacts.types.date_time.serialize_aws_json_1_1(
        value["receipt_time"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Receipt:
    out: Receipt = {}  # type: ignore[typeddict-item]
    if "ContactChannelArn" in data:
        out["contact_channel_arn"] = data["ContactChannelArn"]
    if "ReceiptType" in data:
        import aws_sdk_ssm_contacts.types.receipt_type

        out["receipt_type"] = (
            aws_sdk_ssm_contacts.types.receipt_type.deserialize_aws_json_1_1(
                data["ReceiptType"]
            )
        )
    else:
        raise DeserializationError("Receipt.receipt_type required")
    if "ReceiptInfo" in data:
        out["receipt_info"] = data["ReceiptInfo"]
    if "ReceiptTime" in data:
        import aws_sdk_ssm_contacts.types.date_time

        out["receipt_time"] = (
            aws_sdk_ssm_contacts.types.date_time.deserialize_aws_json_1_1(
                data["ReceiptTime"]
            )
        )
    else:
        raise DeserializationError("Receipt.receipt_time required")
    return out
