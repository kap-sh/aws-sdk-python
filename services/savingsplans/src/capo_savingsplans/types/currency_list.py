"""Generated from Smithy shape ``com.amazonaws.savingsplans#CurrencyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.currency_code

CurrencyList: TypeAlias = list["capo_savingsplans.types.currency_code.CurrencyCode"]


# --- restJson1 ser/de ---
def serialize_json(value: CurrencyList) -> list:
    import capo_savingsplans.types.currency_code

    out: list = []
    for item in value:
        out.append(capo_savingsplans.types.currency_code.serialize_json(item))
    return out


def deserialize_json(data: list) -> CurrencyList:
    import capo_savingsplans.types.currency_code

    out: CurrencyList = []
    for item in data:
        out.append(capo_savingsplans.types.currency_code.deserialize_json(item))
    return out
