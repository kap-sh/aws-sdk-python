"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#ReceiptsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ssm_contacts.types.receipt

ReceiptsList: TypeAlias = list["aws_sdk_ssm_contacts.types.receipt.Receipt"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReceiptsList) -> list:
    import aws_sdk_ssm_contacts.types.receipt

    out: list = []
    for item in value:
        out.append(aws_sdk_ssm_contacts.types.receipt.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ReceiptsList:
    import aws_sdk_ssm_contacts.types.receipt

    out: ReceiptsList = []
    for item in data:
        out.append(aws_sdk_ssm_contacts.types.receipt.deserialize_aws_json_1_1(item))
    return out
