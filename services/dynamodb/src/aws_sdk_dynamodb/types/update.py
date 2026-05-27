"""Generated from Smithy shape ``com.amazonaws.dynamodb#Update``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.condition_expression
    import aws_sdk_dynamodb.types.expression_attribute_name_map
    import aws_sdk_dynamodb.types.expression_attribute_value_map
    import aws_sdk_dynamodb.types.key
    import aws_sdk_dynamodb.types.return_values_on_condition_check_failure
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.update_expression


class Update(TypedDict):
    key: "aws_sdk_dynamodb.types.key.Key"
    """<p>The primary key of the item to be updated. Each element consists of an attribute name and a value for that attribute.</p>"""
    update_expression: "aws_sdk_dynamodb.types.update_expression.UpdateExpression"
    """<p>An expression that defines one or more attributes to be updated, the action to be performed on them, and new value(s) for them.</p>"""
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>Name of the table for the <code>UpdateItem</code> request. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    condition_expression: NotRequired[
        "aws_sdk_dynamodb.types.condition_expression.ConditionExpression"
    ]
    """<p>A condition that must be satisfied in order for a conditional update to succeed.</p>"""
    expression_attribute_names: NotRequired[
        "aws_sdk_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
    ]
    """<p>One or more substitution tokens for attribute names in an expression.</p>"""
    expression_attribute_values: NotRequired[
        "aws_sdk_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
    ]
    """<p>One or more values that can be substituted in an expression.</p>"""
    return_values_on_condition_check_failure: NotRequired[
        "aws_sdk_dynamodb.types.return_values_on_condition_check_failure.ReturnValuesOnConditionCheckFailure"
    ]
    """<p>Use <code>ReturnValuesOnConditionCheckFailure</code> to get the item attributes if the <code>Update</code> condition fails. For <code>ReturnValuesOnConditionCheckFailure</code>, the valid values are: NONE and ALL_OLD.</p>"""
