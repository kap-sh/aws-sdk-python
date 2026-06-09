"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactGetItem``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.get


class TransactGetItem(TypedDict):
    get: "aws_sdk_dynamodb.types.get.Get"
    """<p>Contains the primary key that identifies the item to get, together with the name of the table that contains the item, and optionally the specific attributes of the item to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransactGetItem) -> dict:
    out: dict = {}
    import aws_sdk_dynamodb.types.get

    out["Get"] = aws_sdk_dynamodb.types.get.serialize_aws_json_1_0(value["get"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TransactGetItem:
    out: TransactGetItem = {}  # type: ignore[typeddict-item]
    if "Get" in data:
        import aws_sdk_dynamodb.types.get

        out["get"] = aws_sdk_dynamodb.types.get.deserialize_aws_json_1_0(data["Get"])
    else:
        raise DeserializationError("TransactGetItem.get required")
    return out
