"""Generated from Smithy shape ``com.amazonaws.ssm#InventoryAggregator``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.inventory_aggregator_expression
    import aws_sdk_ssm.types.inventory_aggregator_list
    import aws_sdk_ssm.types.inventory_group_list


class InventoryAggregator(TypedDict):
    expression: NotRequired[
        "aws_sdk_ssm.types.inventory_aggregator_expression.InventoryAggregatorExpression"
    ]
    """<p>The inventory type and attribute name for aggregation.</p>"""
    aggregators: NotRequired[
        "aws_sdk_ssm.types.inventory_aggregator_list.InventoryAggregatorList"
    ]
    """<p>Nested aggregators to further refine aggregation for an inventory type.</p>"""
    groups: NotRequired["aws_sdk_ssm.types.inventory_group_list.InventoryGroupList"]
    """<p>A user-defined set of one or more filters on which to aggregate inventory data. Groups return a count of resources that match and don't match the specified criteria.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InventoryAggregator) -> dict:
    out: dict = {}
    if "expression" in value:
        out["Expression"] = value["expression"]
    if "aggregators" in value:
        import aws_sdk_ssm.types.inventory_aggregator_list

        out["Aggregators"] = (
            aws_sdk_ssm.types.inventory_aggregator_list.serialize_aws_json_1_1(
                value["aggregators"]
            )
        )
    if "groups" in value:
        import aws_sdk_ssm.types.inventory_group_list

        out["Groups"] = aws_sdk_ssm.types.inventory_group_list.serialize_aws_json_1_1(
            value["groups"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InventoryAggregator:
    out: InventoryAggregator = {}  # type: ignore[typeddict-item]
    if "Expression" in data:
        out["expression"] = data["Expression"]
    if "Aggregators" in data:
        import aws_sdk_ssm.types.inventory_aggregator_list

        out["aggregators"] = (
            aws_sdk_ssm.types.inventory_aggregator_list.deserialize_aws_json_1_1(
                data["Aggregators"]
            )
        )
    if "Groups" in data:
        import aws_sdk_ssm.types.inventory_group_list

        out["groups"] = aws_sdk_ssm.types.inventory_group_list.deserialize_aws_json_1_1(
            data["Groups"]
        )
    return out
