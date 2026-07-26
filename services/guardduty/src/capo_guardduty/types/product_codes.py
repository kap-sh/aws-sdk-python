"""Generated from Smithy shape ``com.amazonaws.guardduty#ProductCodes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.product_code

ProductCodes: TypeAlias = list["capo_guardduty.types.product_code.ProductCode"]


# --- restJson1 ser/de ---
def serialize_json(value: ProductCodes) -> list:
    import capo_guardduty.types.product_code

    out: list = []
    for item in value:
        out.append(capo_guardduty.types.product_code.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProductCodes:
    import capo_guardduty.types.product_code

    out: ProductCodes = []
    for item in data:
        out.append(capo_guardduty.types.product_code.deserialize_json(item))
    return out
