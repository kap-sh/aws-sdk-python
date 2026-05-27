"""Generated from Smithy shape ``com.amazonaws.dynamodb#ConditionCheck``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.condition_expression
    import aws_sdk_dynamodb.types.expression_attribute_name_map
    import aws_sdk_dynamodb.types.expression_attribute_value_map
    import aws_sdk_dynamodb.types.key
    import aws_sdk_dynamodb.types.return_values_on_condition_check_failure
    import aws_sdk_dynamodb.types.table_arn


class ConditionCheck(TypedDict):
    key: "aws_sdk_dynamodb.types.key.Key"
    """<p>The primary key of the item to be checked. Each element consists of an attribute name and a value for that attribute.</p>"""
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>Name of the table for the check item request. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    condition_expression: (
        "aws_sdk_dynamodb.types.condition_expression.ConditionExpression"
    )
    """<p>A condition that must be satisfied in order for a conditional update to succeed. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html\">Condition expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expression_attribute_names: NotRequired[
        "aws_sdk_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
    ]
    """<p>One or more substitution tokens for attribute names in an expression. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ExpressionAttributeNames.html\">Expression attribute names</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    expression_attribute_values: NotRequired[
        "aws_sdk_dynamodb.types.expression_attribute_value_map.ExpressionAttributeValueMap"
    ]
    """<p>One or more values that can be substituted in an expression. For more information, see <a href=\"https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html\">Condition expressions</a> in the <i>Amazon DynamoDB Developer Guide</i>.</p>"""
    return_values_on_condition_check_failure: NotRequired[
        "aws_sdk_dynamodb.types.return_values_on_condition_check_failure.ReturnValuesOnConditionCheckFailure"
    ]
    """<p>Use <code>ReturnValuesOnConditionCheckFailure</code> to get the item attributes if the <code>ConditionCheck</code> condition fails. For <code>ReturnValuesOnConditionCheckFailure</code>, the valid values are: NONE and ALL_OLD.</p>"""
