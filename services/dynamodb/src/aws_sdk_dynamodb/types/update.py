"""Generated from Smithy shape ``com.amazonaws.dynamodb#Update``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.condition_expression
    import aws_sdk_dynamodb.types.expression_attribute_name_map
    import aws_sdk_dynamodb.types.expression_attribute_value_map
    import aws_sdk_dynamodb.types.key
    import aws_sdk_dynamodb.types.return_values_on_condition_check_failure
    import aws_sdk_dynamodb.types.table_arn
    import aws_sdk_dynamodb.types.update_expression


class Update(TypedDict, closed=True):
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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Update) -> dict:
    out: dict = {}
    import aws_sdk_dynamodb.types.key

    out["Key"] = aws_sdk_dynamodb.types.key.serialize_aws_json_1_0(value["key"])
    out["UpdateExpression"] = value["update_expression"]
    out["TableName"] = value["table_name"]
    if "condition_expression" in value:
        out["ConditionExpression"] = value["condition_expression"]
    if "expression_attribute_names" in value:
        import aws_sdk_dynamodb.types.expression_attribute_name_map

        out["ExpressionAttributeNames"] = (
            aws_sdk_dynamodb.types.expression_attribute_name_map.serialize_aws_json_1_0(
                value["expression_attribute_names"]
            )
        )
    if "expression_attribute_values" in value:
        import aws_sdk_dynamodb.types.expression_attribute_value_map

        out["ExpressionAttributeValues"] = (
            aws_sdk_dynamodb.types.expression_attribute_value_map.serialize_aws_json_1_0(
                value["expression_attribute_values"]
            )
        )
    if "return_values_on_condition_check_failure" in value:
        import aws_sdk_dynamodb.types.return_values_on_condition_check_failure

        out["ReturnValuesOnConditionCheckFailure"] = (
            aws_sdk_dynamodb.types.return_values_on_condition_check_failure.serialize_aws_json_1_0(
                value["return_values_on_condition_check_failure"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Update:
    out: Update = {}  # type: ignore[typeddict-item]
    if "Key" in data:
        import aws_sdk_dynamodb.types.key

        out["key"] = aws_sdk_dynamodb.types.key.deserialize_aws_json_1_0(data["Key"])
    else:
        raise DeserializationError("Update.key required")
    if "UpdateExpression" in data:
        out["update_expression"] = data["UpdateExpression"]
    else:
        raise DeserializationError("Update.update_expression required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("Update.table_name required")
    if "ConditionExpression" in data:
        out["condition_expression"] = data["ConditionExpression"]
    if "ExpressionAttributeNames" in data:
        import aws_sdk_dynamodb.types.expression_attribute_name_map

        out["expression_attribute_names"] = (
            aws_sdk_dynamodb.types.expression_attribute_name_map.deserialize_aws_json_1_0(
                data["ExpressionAttributeNames"]
            )
        )
    if "ExpressionAttributeValues" in data:
        import aws_sdk_dynamodb.types.expression_attribute_value_map

        out["expression_attribute_values"] = (
            aws_sdk_dynamodb.types.expression_attribute_value_map.deserialize_aws_json_1_0(
                data["ExpressionAttributeValues"]
            )
        )
    if "ReturnValuesOnConditionCheckFailure" in data:
        import aws_sdk_dynamodb.types.return_values_on_condition_check_failure

        out["return_values_on_condition_check_failure"] = (
            aws_sdk_dynamodb.types.return_values_on_condition_check_failure.deserialize_aws_json_1_0(
                data["ReturnValuesOnConditionCheckFailure"]
            )
        )
    return out
