"""Generated from Smithy shape ``com.amazonaws.fsx#RouteTableIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fsx.types.route_table_id

RouteTableIds: TypeAlias = list["capo_fsx.types.route_table_id.RouteTableId"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RouteTableIds) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RouteTableIds:
    return list(data)
