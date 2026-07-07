"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactGetItemsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.return_consumed_capacity
    import aws_sdk_dynamodb.types.transact_get_item_list


class TransactGetItemsInput(TypedDict, closed=True):
    transact_items: "aws_sdk_dynamodb.types.transact_get_item_list.TransactGetItemList"
    """<p>An ordered array of up to 100 <code>TransactGetItem</code> objects, each of which contains a <code>Get</code> structure.</p>"""
    return_consumed_capacity: NotRequired[
        "aws_sdk_dynamodb.types.return_consumed_capacity.ReturnConsumedCapacity"
    ]
    """<p>A value of <code>TOTAL</code> causes consumed capacity information to be returned, and a value of <code>NONE</code> prevents that information from being returned. No other value is valid.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransactGetItemsInput) -> dict:
    out: dict = {}
    import aws_sdk_dynamodb.types.transact_get_item_list

    out["TransactItems"] = (
        aws_sdk_dynamodb.types.transact_get_item_list.serialize_aws_json_1_0(
            value["transact_items"]
        )
    )
    if "return_consumed_capacity" in value:
        import aws_sdk_dynamodb.types.return_consumed_capacity

        out["ReturnConsumedCapacity"] = (
            aws_sdk_dynamodb.types.return_consumed_capacity.serialize_aws_json_1_0(
                value["return_consumed_capacity"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TransactGetItemsInput:
    out: TransactGetItemsInput = {}  # type: ignore[typeddict-item]
    if "TransactItems" in data:
        import aws_sdk_dynamodb.types.transact_get_item_list

        out["transact_items"] = (
            aws_sdk_dynamodb.types.transact_get_item_list.deserialize_aws_json_1_0(
                data["TransactItems"]
            )
        )
    else:
        raise DeserializationError("TransactGetItemsInput.transact_items required")
    if "ReturnConsumedCapacity" in data:
        import aws_sdk_dynamodb.types.return_consumed_capacity

        out["return_consumed_capacity"] = (
            aws_sdk_dynamodb.types.return_consumed_capacity.deserialize_aws_json_1_0(
                data["ReturnConsumedCapacity"]
            )
        )
    return out
