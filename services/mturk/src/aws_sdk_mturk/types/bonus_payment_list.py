"""Generated from Smithy shape ``com.amazonaws.mturk#BonusPaymentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mturk.types.bonus_payment

BonusPaymentList: TypeAlias = list["aws_sdk_mturk.types.bonus_payment.BonusPayment"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BonusPaymentList) -> list:
    import aws_sdk_mturk.types.bonus_payment

    out: list = []
    for item in value:
        out.append(aws_sdk_mturk.types.bonus_payment.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BonusPaymentList:
    import aws_sdk_mturk.types.bonus_payment

    out: BonusPaymentList = []
    for item in data:
        out.append(aws_sdk_mturk.types.bonus_payment.deserialize_aws_json_1_1(item))
    return out
