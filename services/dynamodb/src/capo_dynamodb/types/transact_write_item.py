"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactWriteItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.condition_check
    import capo_dynamodb.types.delete
    import capo_dynamodb.types.put
    import capo_dynamodb.types.update


class TransactWriteItem(TypedDict, closed=True):
    condition_check: NotRequired["capo_dynamodb.types.condition_check.ConditionCheck"]
    """<p>A request to perform a check item operation.</p>"""
    put: NotRequired["capo_dynamodb.types.put.Put"]
    """<p>A request to perform a <code>PutItem</code> operation.</p>"""
    delete: NotRequired["capo_dynamodb.types.delete.Delete"]
    """<p>A request to perform a <code>DeleteItem</code> operation.</p>"""
    update: NotRequired["capo_dynamodb.types.update.Update"]
    """<p>A request to perform an <code>UpdateItem</code> operation.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransactWriteItem) -> dict:
    out: dict = {}
    if "condition_check" in value:
        import capo_dynamodb.types.condition_check

        out["ConditionCheck"] = (
            capo_dynamodb.types.condition_check.serialize_aws_json_1_0(
                value["condition_check"]
            )
        )
    if "put" in value:
        import capo_dynamodb.types.put

        out["Put"] = capo_dynamodb.types.put.serialize_aws_json_1_0(value["put"])
    if "delete" in value:
        import capo_dynamodb.types.delete

        out["Delete"] = capo_dynamodb.types.delete.serialize_aws_json_1_0(
            value["delete"]
        )
    if "update" in value:
        import capo_dynamodb.types.update

        out["Update"] = capo_dynamodb.types.update.serialize_aws_json_1_0(
            value["update"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> TransactWriteItem:
    out: TransactWriteItem = {}  # type: ignore[typeddict-item]
    if data.get("ConditionCheck") is not None:
        import capo_dynamodb.types.condition_check

        out["condition_check"] = (
            capo_dynamodb.types.condition_check.deserialize_aws_json_1_0(
                data["ConditionCheck"]
            )
        )
    if data.get("Put") is not None:
        import capo_dynamodb.types.put

        out["put"] = capo_dynamodb.types.put.deserialize_aws_json_1_0(data["Put"])
    if data.get("Delete") is not None:
        import capo_dynamodb.types.delete

        out["delete"] = capo_dynamodb.types.delete.deserialize_aws_json_1_0(
            data["Delete"]
        )
    if data.get("Update") is not None:
        import capo_dynamodb.types.update

        out["update"] = capo_dynamodb.types.update.deserialize_aws_json_1_0(
            data["Update"]
        )
    return out
