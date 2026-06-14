"""Generated from Smithy shape ``com.amazonaws.costexplorer#CostCategoryRule``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.cost_category_inherited_value_dimension
    import aws_sdk_cost_explorer.types.cost_category_rule_type
    import aws_sdk_cost_explorer.types.cost_category_value
    import aws_sdk_cost_explorer.types.expression


class CostCategoryRule(TypedDict):
    value: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_value.CostCategoryValue"
    ]
    rule: NotRequired["aws_sdk_cost_explorer.types.expression.Expression"]
    r"""<p>An <a href=\"https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_Expression.html\">Expression</a> object used to categorize costs. This supports dimensions, tags, and nested expressions. Currently the only dimensions supported are <code>LINKED_ACCOUNT</code>, <code>SERVICE_CODE</code>, <code>RECORD_TYPE</code>, <code>LINKED_ACCOUNT_NAME</code>, <code>REGION</code>, and <code>USAGE_TYPE</code>.</p> <p> <code>RECORD_TYPE</code> is a dimension used for Cost Explorer APIs, and is also supported for cost category expressions. This dimension uses different terms, depending on whether you're using the console or API/JSON editor. For a detailed comparison, see <a href=\"https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/manage-cost-categories.html#cost-categories-terms\">Term Comparisons</a> in the <i>Billing and Cost Management User Guide</i>.</p>"""
    inherited_value: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_inherited_value_dimension.CostCategoryInheritedValueDimension"
    ]
    """<p>The value the line item is categorized as if the line item contains the matched dimension.</p>"""
    type: NotRequired[
        "aws_sdk_cost_explorer.types.cost_category_rule_type.CostCategoryRuleType"
    ]
    """<p>You can define the <code>CostCategoryRule</code> rule type as either <code>REGULAR</code> or <code>INHERITED_VALUE</code>. The <code>INHERITED_VALUE</code> rule type adds the flexibility to define a rule that dynamically inherits the cost category value. This value is from the dimension value that's defined by <code>CostCategoryInheritedValueDimension</code>. For example, suppose that you want to costs to be dynamically grouped based on the value of a specific tag key. First, choose an inherited value rule type, and then choose the tag dimension and specify the tag key to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CostCategoryRule) -> dict:
    out: dict = {}
    if "value" in value:
        out["Value"] = value["value"]
    if "rule" in value:
        import aws_sdk_cost_explorer.types.expression

        out["Rule"] = aws_sdk_cost_explorer.types.expression.serialize_aws_json_1_1(
            value["rule"]
        )
    if "inherited_value" in value:
        import aws_sdk_cost_explorer.types.cost_category_inherited_value_dimension

        out["InheritedValue"] = (
            aws_sdk_cost_explorer.types.cost_category_inherited_value_dimension.serialize_aws_json_1_1(
                value["inherited_value"]
            )
        )
    if "type" in value:
        import aws_sdk_cost_explorer.types.cost_category_rule_type

        out["Type"] = (
            aws_sdk_cost_explorer.types.cost_category_rule_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CostCategoryRule:
    out: CostCategoryRule = {}  # type: ignore[typeddict-item]
    if "Value" in data:
        out["value"] = data["Value"]
    if "Rule" in data:
        import aws_sdk_cost_explorer.types.expression

        out["rule"] = aws_sdk_cost_explorer.types.expression.deserialize_aws_json_1_1(
            data["Rule"]
        )
    if "InheritedValue" in data:
        import aws_sdk_cost_explorer.types.cost_category_inherited_value_dimension

        out["inherited_value"] = (
            aws_sdk_cost_explorer.types.cost_category_inherited_value_dimension.deserialize_aws_json_1_1(
                data["InheritedValue"]
            )
        )
    if "Type" in data:
        import aws_sdk_cost_explorer.types.cost_category_rule_type

        out["type"] = (
            aws_sdk_cost_explorer.types.cost_category_rule_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    return out
