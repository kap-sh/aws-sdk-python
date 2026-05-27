"""Generated from Smithy shape ``com.amazonaws.dynamodb#Get``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.expression_attribute_name_map
    import aws_sdk_dynamodb.types.key
    import aws_sdk_dynamodb.types.projection_expression
    import aws_sdk_dynamodb.types.table_arn


class Get(TypedDict):
    key: "aws_sdk_dynamodb.types.key.Key"
    """<p>A map of attribute names to <code>AttributeValue</code> objects that specifies the primary key of the item to retrieve.</p>"""
    table_name: "aws_sdk_dynamodb.types.table_arn.TableArn"
    """<p>The name of the table from which to retrieve the specified item. You can also provide the Amazon Resource Name (ARN) of the table in this parameter.</p>"""
    projection_expression: NotRequired[
        "aws_sdk_dynamodb.types.projection_expression.ProjectionExpression"
    ]
    """<p>A string that identifies one or more attributes of the specified item to retrieve from the table. The attributes in the expression must be separated by commas. If no attribute names are specified, then all attributes of the specified item are returned. If any of the requested attributes are not found, they do not appear in the result.</p>"""
    expression_attribute_names: NotRequired[
        "aws_sdk_dynamodb.types.expression_attribute_name_map.ExpressionAttributeNameMap"
    ]
    """<p>One or more substitution tokens for attribute names in the ProjectionExpression parameter.</p>"""
