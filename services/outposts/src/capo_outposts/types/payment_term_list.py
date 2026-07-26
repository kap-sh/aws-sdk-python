"""Generated from Smithy shape ``com.amazonaws.outposts#PaymentTermList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.payment_term

PaymentTermList: TypeAlias = list["capo_outposts.types.payment_term.PaymentTerm"]


# --- restJson1 ser/de ---
def serialize_json(value: PaymentTermList) -> list:
    import capo_outposts.types.payment_term

    out: list = []
    for item in value:
        out.append(capo_outposts.types.payment_term.serialize_json(item))
    return out


def deserialize_json(data: list) -> PaymentTermList:
    import capo_outposts.types.payment_term

    out: PaymentTermList = []
    for item in data:
        out.append(capo_outposts.types.payment_term.deserialize_json(item))
    return out
