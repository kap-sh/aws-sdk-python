"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemCollectionMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dynamodb.types.item_collection_key_attribute_map
    import capo_dynamodb.types.item_collection_size_estimate_range


class ItemCollectionMetrics(TypedDict, closed=True):
    item_collection_key: NotRequired[
        "capo_dynamodb.types.item_collection_key_attribute_map.ItemCollectionKeyAttributeMap"
    ]
    """<p>The partition key value of the item collection. This value is the same as the partition key value of the item.</p>"""
    size_estimate_range_gb: NotRequired[
        "capo_dynamodb.types.item_collection_size_estimate_range.ItemCollectionSizeEstimateRange"
    ]
    """<p>An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit.</p> <p>The estimate is subject to change over time; therefore, do not rely on the precision or accuracy of the estimate.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ItemCollectionMetrics) -> dict:
    out: dict = {}
    if "item_collection_key" in value:
        import capo_dynamodb.types.item_collection_key_attribute_map

        out["ItemCollectionKey"] = (
            capo_dynamodb.types.item_collection_key_attribute_map.serialize_aws_json_1_0(
                value["item_collection_key"]
            )
        )
    if "size_estimate_range_gb" in value:
        import capo_dynamodb.types.item_collection_size_estimate_range

        out["SizeEstimateRangeGB"] = (
            capo_dynamodb.types.item_collection_size_estimate_range.serialize_aws_json_1_0(
                value["size_estimate_range_gb"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ItemCollectionMetrics:
    out: ItemCollectionMetrics = {}  # type: ignore[typeddict-item]
    if data.get("ItemCollectionKey") is not None:
        import capo_dynamodb.types.item_collection_key_attribute_map

        out["item_collection_key"] = (
            capo_dynamodb.types.item_collection_key_attribute_map.deserialize_aws_json_1_0(
                data["ItemCollectionKey"]
            )
        )
    if data.get("SizeEstimateRangeGB") is not None:
        import capo_dynamodb.types.item_collection_size_estimate_range

        out["size_estimate_range_gb"] = (
            capo_dynamodb.types.item_collection_size_estimate_range.deserialize_aws_json_1_0(
                data["SizeEstimateRangeGB"]
            )
        )
    return out
