"""Generated from Smithy shape ``com.amazonaws.dynamodb#Get``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.expression_attribute_name_map
    import aws_sdk_dynamodb.types.key
    import aws_sdk_dynamodb.types.projection_expression
    import aws_sdk_dynamodb.types.table_arn


class Get(TypedDict, closed=True):
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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Get) -> dict:
    out: dict = {}
    import aws_sdk_dynamodb.types.key

    out["Key"] = aws_sdk_dynamodb.types.key.serialize_aws_json_1_0(value["key"])
    out["TableName"] = value["table_name"]
    if "projection_expression" in value:
        out["ProjectionExpression"] = value["projection_expression"]
    if "expression_attribute_names" in value:
        import aws_sdk_dynamodb.types.expression_attribute_name_map

        out["ExpressionAttributeNames"] = (
            aws_sdk_dynamodb.types.expression_attribute_name_map.serialize_aws_json_1_0(
                value["expression_attribute_names"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Get:
    out: Get = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_dynamodb.types.key

        out["key"] = aws_sdk_dynamodb.types.key.deserialize_aws_json_1_0(data["Key"])
    else:
        raise DeserializationError("Get.key required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("Get.table_name required")
    if "ProjectionExpression" in data:
        out["projection_expression"] = data["ProjectionExpression"]
    if "ExpressionAttributeNames" in data:
        import aws_sdk_dynamodb.types.expression_attribute_name_map

        out["expression_attribute_names"] = (
            aws_sdk_dynamodb.types.expression_attribute_name_map.deserialize_aws_json_1_0(
                data["ExpressionAttributeNames"]
            )
        )
    return out
