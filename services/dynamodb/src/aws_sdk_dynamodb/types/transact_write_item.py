"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactWriteItem``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.condition_check
    import aws_sdk_dynamodb.types.delete
    import aws_sdk_dynamodb.types.put
    import aws_sdk_dynamodb.types.update


class TransactWriteItem(TypedDict):
    condition_check: NotRequired[
        "aws_sdk_dynamodb.types.condition_check.ConditionCheck"
    ]
    """<p>A request to perform a check item operation.</p>"""
    put: NotRequired["aws_sdk_dynamodb.types.put.Put"]
    """<p>A request to perform a <code>PutItem</code> operation.</p>"""
    delete: NotRequired["aws_sdk_dynamodb.types.delete.Delete"]
    """<p>A request to perform a <code>DeleteItem</code> operation.</p>"""
    update: NotRequired["aws_sdk_dynamodb.types.update.Update"]
    """<p>A request to perform an <code>UpdateItem</code> operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransactWriteItem) -> dict:
    out: dict = {}
    if "condition_check" in value:
        import aws_sdk_dynamodb.types.condition_check

        out["ConditionCheck"] = (
            aws_sdk_dynamodb.types.condition_check.serialize_aws_json_1_0(
                value["condition_check"]
            )
        )
    if "put" in value:
        import aws_sdk_dynamodb.types.put

        out["Put"] = aws_sdk_dynamodb.types.put.serialize_aws_json_1_0(value["put"])
    if "delete" in value:
        import aws_sdk_dynamodb.types.delete

        out["Delete"] = aws_sdk_dynamodb.types.delete.serialize_aws_json_1_0(
            value["delete"]
        )
    if "update" in value:
        import aws_sdk_dynamodb.types.update

        out["Update"] = aws_sdk_dynamodb.types.update.serialize_aws_json_1_0(
            value["update"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TransactWriteItem:
    out: TransactWriteItem = {}  # type: ignore[typeddict-item]
    if "ConditionCheck" in data:
        import aws_sdk_dynamodb.types.condition_check

        out["condition_check"] = (
            aws_sdk_dynamodb.types.condition_check.deserialize_aws_json_1_0(
                data["ConditionCheck"]
            )
        )
    if "Put" in data:
        import aws_sdk_dynamodb.types.put

        out["put"] = aws_sdk_dynamodb.types.put.deserialize_aws_json_1_0(data["Put"])
    if "Delete" in data:
        import aws_sdk_dynamodb.types.delete

        out["delete"] = aws_sdk_dynamodb.types.delete.deserialize_aws_json_1_0(
            data["Delete"]
        )
    if "Update" in data:
        import aws_sdk_dynamodb.types.update

        out["update"] = aws_sdk_dynamodb.types.update.deserialize_aws_json_1_0(
            data["Update"]
        )
    return out
