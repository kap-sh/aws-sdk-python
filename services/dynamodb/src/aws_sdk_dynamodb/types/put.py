"""Generated from Smithy shape ``com.amazonaws.dynamodb#Put``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_dynamodb.errors import DeserializationError

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


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Put) -> dict:
    out: dict = {}
    import aws_sdk_dynamodb.types.put_item_input_attribute_map

    out["Item"] = (
        aws_sdk_dynamodb.types.put_item_input_attribute_map.serialize_aws_json_1_0(
            value["item"]
        )
    )
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


def deserialize_aws_json_1_0(data: dict) -> Put:
    out: Put = {}  # type: ignore[typeddict-item]
    if "Item" in data:
        import aws_sdk_dynamodb.types.put_item_input_attribute_map

        out["item"] = (
            aws_sdk_dynamodb.types.put_item_input_attribute_map.deserialize_aws_json_1_0(
                data["Item"]
            )
        )
    else:
        raise DeserializationError("Put.item required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("Put.table_name required")
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
