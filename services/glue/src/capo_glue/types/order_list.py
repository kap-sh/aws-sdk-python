"""Generated from Smithy shape ``com.amazonaws.glue#OrderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.order

OrderList: TypeAlias = list["capo_glue.types.order.Order"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrderList) -> list:
    import capo_glue.types.order

    out: list = []
    for item in value:
        out.append(capo_glue.types.order.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> OrderList:
    import capo_glue.types.order

    out: OrderList = []
    for item in data:
        out.append(capo_glue.types.order.deserialize_aws_json_1_1(item))
    return out
