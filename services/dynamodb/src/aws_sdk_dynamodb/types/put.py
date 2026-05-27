"""Generated from Smithy shape ``com.amazonaws.dynamodb#Put``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.condition_expression
    import aws_sdk_dynamodb.types.expression_attribute_name_map
    import aws_sdk_dynamodb.types.expression_attribute_value_map
    import aws_sdk_dynamodb.types.put_item_input_attribute_map
    import aws_sdk_dynamodb.types.return_values_on_condition_check_failure
    import aws_sdk_dynamodb.types.table_arn


class Put(TypedDict):
    item: "aws_sdk_dynamodb.types.put_item_input_attribute_map.PutItemInputAttributeMap"
    """<p>A map of attribute name to attribute values, representing the primary key of the item to be written by <code>PutItem</code>. All of the table's primary key attributes must be specified, and their data types must match those of the table's key schema. If any attributes are present in the item that are part of an index key schema for the table, their types must match the index key schema. </p>"""
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>Name of the table in which to write the item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
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
    """<p>Use <code>ReturnValuesOnConditionCheckFailure</code> to get the item attributes if the <code>Put</code> condition fails. For <code>ReturnValuesOnConditionCheckFailure</code>, the valid values are: NONE and ALL_OLD.</p>"""
