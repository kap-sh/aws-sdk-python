"""Generated from Smithy shape ``com.amazonaws.outposts#PaymentOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.payment_option

PaymentOptionList: TypeAlias = list[
    "aws_sdk_outposts.types.payment_option.PaymentOption"
]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentOptionList) -> list:
    import aws_sdk_outposts.types.payment_option

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.payment_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> PaymentOptionList:
    import aws_sdk_outposts.types.payment_option

    out: PaymentOptionList = []
    for item in data:
        out.append(aws_sdk_outposts.types.payment_option.deserialize_json(item))
    return out
