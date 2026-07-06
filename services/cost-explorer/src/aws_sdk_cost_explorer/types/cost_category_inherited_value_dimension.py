"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryInheritedValueDimension``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_inherited_value_dimension_name
    import aws_sdk_cost_explorer.types.generic_string


class CostCategoryInheritedValueDimension(TypedDict, closed=True):
    dimension_name: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_inherited_value_dimension_name.CostCategoryInheritedValueDimensionName"
    ]
    """<p>The name of the dimension that's used to group costs.</p> <p>If you specify <code>LINKED_ACCOUNT_NAME</code>, the cost category value is based on account name. If you specify <code>TAG</code>, the cost category value is based on the value of the specified tag key.</p>"""
    dimension_key: NotRequired[
        "aws_sdk_cost_explorer.types.generic_string.GenericString"
    ]
    """<p>The key to extract cost category values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryInheritedValueDimension) -> dict:
    out: dict = {}
    if "dimension_name" in value:
        import aws_sdk_cost_explorer.types.cost_category_inherited_value_dimension_name

        out["DimensionName"] = (
            aws_sdk_cost_explorer.types.cost_category_inherited_value_dimension_name.serialize_aws_json_1_1(
                value["dimension_name"]
            )
        )
    if "dimension_key" in value:
        out["DimensionKey"] = value["dimension_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CostCategoryInheritedValueDimension:
    out: CostCategoryInheritedValueDimension = {}  # type: ignore[typeddict-item]
    if "DimensionName" in data:
        import aws_sdk_cost_explorer.types.cost_category_inherited_value_dimension_name

        out["dimension_name"] = (
            aws_sdk_cost_explorer.types.cost_category_inherited_value_dimension_name.deserialize_aws_json_1_1(
                data["DimensionName"]
            )
        )
    if "DimensionKey" in data:
        out["dimension_key"] = data["DimensionKey"]
    return out
