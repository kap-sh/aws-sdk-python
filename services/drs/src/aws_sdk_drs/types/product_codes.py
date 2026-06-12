"""Generated from Smithy shape ``com.amazonaws.drs#ProductCodes``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_drs.types.product_code

ProductCodes: TypeAlias = list["aws_sdk_drs.types.product_code.ProductCode"]


# --- restJson1 ser/de ---
def serialize_json(value: ProductCodes) -> list:
    import aws_sdk_drs.types.product_code
    out: list = []
    for item in value:
        out.append(aws_sdk_drs.types.product_code.serialize_json(item))
    return out


def deserialize_json(data: list) -> ProductCodes:
    import aws_sdk_drs.types.product_code
    out: ProductCodes = []
    for item in data:
        out.append(aws_sdk_drs.types.product_code.deserialize_json(item))
    return out