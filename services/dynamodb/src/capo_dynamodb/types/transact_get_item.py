"""Generated from Smithy shape ``com.amazonaws.dynamodb#TransactGetItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_dynamodb.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dynamodb.types.get


class TransactGetItem(TypedDict, closed=True):
    get: "capo_dynamodb.types.get.Get"
    """<p>Contains the primary key that identifies the item to get, together with the name of the table that contains the item, and optionally the specific attributes of the item to retrieve.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransactGetItem) -> dict:
    out: dict = {}
    import capo_dynamodb.types.get

    out["Get"] = capo_dynamodb.types.get.serialize_aws_json_1_0(value["get"])
    return out


def deserialize_aws_json_1_0(data: dict) -> TransactGetItem:
    out: TransactGetItem = {}  # type: ignore[typeddict-item]
    if data.get("Get") is not None:
        import capo_dynamodb.types.get

        out["get"] = capo_dynamodb.types.get.deserialize_aws_json_1_0(data["Get"])
    else:
        raise DeserializationError("TransactGetItem.get required")
    return out
