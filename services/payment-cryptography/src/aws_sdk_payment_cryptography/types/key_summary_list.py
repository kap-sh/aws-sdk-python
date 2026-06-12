"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#KeySummaryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.key_summary

KeySummaryList: TypeAlias = list[
    "aws_sdk_payment_cryptography.types.key_summary.KeySummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeySummaryList) -> list:
    import aws_sdk_payment_cryptography.types.key_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_payment_cryptography.types.key_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> KeySummaryList:
    import aws_sdk_payment_cryptography.types.key_summary

    out: KeySummaryList = []
    for item in data:
        out.append(
            aws_sdk_payment_cryptography.types.key_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out
