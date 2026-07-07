"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CollectionGroupCapacityLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.collection_group_max_indexing_capacity_value
    import aws_sdk_opensearchserverless.types.collection_group_max_search_capacity_value
    import aws_sdk_opensearchserverless.types.collection_group_min_indexing_capacity_value
    import aws_sdk_opensearchserverless.types.collection_group_min_search_capacity_value


class CollectionGroupCapacityLimits(TypedDict, closed=True):
    max_indexing_capacity_in_ocu: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_max_indexing_capacity_value.CollectionGroupMaxIndexingCapacityValue"
    ]
    """<p>The maximum indexing capacity for collections in the group.</p>"""
    max_search_capacity_in_ocu: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_max_search_capacity_value.CollectionGroupMaxSearchCapacityValue"
    ]
    """<p>The maximum search capacity for collections in the group.</p>"""
    min_indexing_capacity_in_ocu: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_min_indexing_capacity_value.CollectionGroupMinIndexingCapacityValue"
    ]
    """<p>The minimum indexing capacity for collections in the group.</p>"""
    min_search_capacity_in_ocu: NotRequired[
        "aws_sdk_opensearchserverless.types.collection_group_min_search_capacity_value.CollectionGroupMinSearchCapacityValue"
    ]
    """<p>The minimum search capacity for collections in the group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionGroupCapacityLimits) -> dict:
    out: dict = {}
    if "max_indexing_capacity_in_ocu" in value:
        out["maxIndexingCapacityInOCU"] = value["max_indexing_capacity_in_ocu"]
    if "max_search_capacity_in_ocu" in value:
        out["maxSearchCapacityInOCU"] = value["max_search_capacity_in_ocu"]
    if "min_indexing_capacity_in_ocu" in value:
        out["minIndexingCapacityInOCU"] = value["min_indexing_capacity_in_ocu"]
    if "min_search_capacity_in_ocu" in value:
        out["minSearchCapacityInOCU"] = value["min_search_capacity_in_ocu"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CollectionGroupCapacityLimits:
    out: CollectionGroupCapacityLimits = {}  # type: ignore[typeddict-item]
    if "maxIndexingCapacityInOCU" in data:
        out["max_indexing_capacity_in_ocu"] = data["maxIndexingCapacityInOCU"]
    if "maxSearchCapacityInOCU" in data:
        out["max_search_capacity_in_ocu"] = data["maxSearchCapacityInOCU"]
    if "minIndexingCapacityInOCU" in data:
        out["min_indexing_capacity_in_ocu"] = data["minIndexingCapacityInOCU"]
    if "minSearchCapacityInOCU" in data:
        out["min_search_capacity_in_ocu"] = data["minSearchCapacityInOCU"]
    return out
