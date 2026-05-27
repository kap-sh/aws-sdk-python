"""Generated from Smithy shape ``com.amazonaws.dynamodb#ItemCollectionMetrics``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_dynamodb.types.item_collection_key_attribute_map
    import aws_sdk_dynamodb.types.item_collection_size_estimate_range


class ItemCollectionMetrics(TypedDict):
    item_collection_key: NotRequired[
        "aws_sdk_dynamodb.types.item_collection_key_attribute_map.ItemCollectionKeyAttributeMap"
    ]
    """<p>The partition key value of the item collection. This value is the same as the partition key value of the item.</p>"""
    size_estimate_range_gb: NotRequired[
        "aws_sdk_dynamodb.types.item_collection_size_estimate_range.ItemCollectionSizeEstimateRange"
    ]
    """<p>An estimate of item collection size, in gigabytes. This value is a two-element array containing a lower bound and an upper bound for the estimate. The estimate includes the size of all the items in the table, plus the size of all attributes projected into all of the local secondary indexes on that table. Use this estimate to measure whether a local secondary index is approaching its size limit.</p> <p>The estimate is subject to change over time; therefore, do not rely on the precision or accuracy of the estimate.</p>"""
