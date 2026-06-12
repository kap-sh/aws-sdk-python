"""Generated from Smithy shape ``com.amazonaws.savingsplans#CurrencyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_savingsplans.types.currency_code

CurrencyList: TypeAlias = list["aws_sdk_savingsplans.types.currency_code.CurrencyCode"]


# --- restJson1 ser/de ---
def serialize_json(value: CurrencyList) -> list:
    import aws_sdk_savingsplans.types.currency_code

    out: list = []
    for item in value:
        out.append(aws_sdk_savingsplans.types.currency_code.serialize_json(item))
    return out


def deserialize_json(data: list) -> CurrencyList:
    import aws_sdk_savingsplans.types.currency_code

    out: CurrencyList = []
    for item in data:
        out.append(aws_sdk_savingsplans.types.currency_code.deserialize_json(item))
    return out
