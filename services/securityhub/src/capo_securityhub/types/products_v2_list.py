"""Generated from Smithy shape ``com.amazonaws.securityhub#ProductsV2List``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.product_v2

ProductsV2List: TypeAlias = list["capo_securityhub.types.product_v2.ProductV2"]


# --- restJson1 ser/de ---
def serialize_json(value: ProductsV2List) -> list:
    import capo_securityhub.types.product_v2

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.product_v2.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProductsV2List:
    import capo_securityhub.types.product_v2

    out: ProductsV2List = []
    for item in data:
        out.append(capo_securityhub.types.product_v2.deserialize_json(item))
    return out
