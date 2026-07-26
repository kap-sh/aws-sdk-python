"""Generated from Smithy shape ``com.amazonaws.outposts#PaymentOptionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.payment_option

PaymentOptionList: TypeAlias = list["capo_outposts.types.payment_option.PaymentOption"]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentOptionList) -> list:
    import capo_outposts.types.payment_option

    out: list = []
    for item in value:
        out.append(capo_outposts.types.payment_option.serialize_json(item))
    return out


def deserialize_json(data: list) -> PaymentOptionList:
    import capo_outposts.types.payment_option

    out: PaymentOptionList = []
    for item in data:
        out.append(capo_outposts.types.payment_option.deserialize_json(item))
    return out
