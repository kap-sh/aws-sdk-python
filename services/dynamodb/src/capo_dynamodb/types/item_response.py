"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.attribute_map


class ItemResponse(TypedDict, closed=True):
    item: NotRequired["capo_dynamodb.types.attribute_map.AttributeMap"]
    """<p>Map of attribute data consisting of the data type and attribute value.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ItemResponse) -> dict:
    out: dict = {}
    if "item" in value:
        import capo_dynamodb.types.attribute_map

        out["Item"] = capo_dynamodb.types.attribute_map.serialize_aws_json_1_0(
            value["item"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ItemResponse:
    out: ItemResponse = {}  # type: ignore[typeddict-item]
    if data.get("Item") is not None:
        import capo_dynamodb.types.attribute_map

        out["item"] = capo_dynamodb.types.attribute_map.deserialize_aws_json_1_0(
            data["Item"]
        )
    return out
