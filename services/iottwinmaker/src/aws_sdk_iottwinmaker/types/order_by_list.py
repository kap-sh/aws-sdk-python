"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#OrderByList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.order_by

OrderByList: TypeAlias = list["aws_sdk_iottwinmaker.types.order_by.OrderBy"]


# --- restJson1 ser/de ---
def serialize_json(value: OrderByList) -> list:
    import aws_sdk_iottwinmaker.types.order_by

    out: list = []
    for item in value:
        out.append(aws_sdk_iottwinmaker.types.order_by.serialize_json(item))
    return out


def deserialize_json(data: list) -> OrderByList:
    import aws_sdk_iottwinmaker.types.order_by

    out: OrderByList = []
    for item in data:
        out.append(aws_sdk_iottwinmaker.types.order_by.deserialize_json(item))
    return out
