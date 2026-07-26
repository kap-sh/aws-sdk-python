"""Generated from Smithy shape ``com.amazonaws.securityhub#ProductsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.product

ProductsList: TypeAlias = list["capo_securityhub.types.product.Product"]


# --- restJson1 ser/de ---
def serialize_json(value: ProductsList) -> list:
    import capo_securityhub.types.product

    out: list = []
    for item in value:
        out.append(capo_securityhub.types.product.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProductsList:
    import capo_securityhub.types.product

    out: ProductsList = []
    for item in data:
        out.append(capo_securityhub.types.product.deserialize_json(item))
    return out
