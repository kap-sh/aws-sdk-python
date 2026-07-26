"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CapacityLimits``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_opensearchserverless.types.indexing_capacity_value
    import capo_opensearchserverless.types.search_capacity_value


class CapacityLimits(TypedDict, closed=True):
    max_indexing_capacity_in_ocu: NotRequired[
        "capo_opensearchserverless.types.indexing_capacity_value.IndexingCapacityValue"
    ]
    """<p>The maximum indexing capacity for collections.</p>"""
    max_search_capacity_in_ocu: NotRequired[
        "capo_opensearchserverless.types.search_capacity_value.SearchCapacityValue"
    ]
    """<p>The maximum search capacity for collections.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapacityLimits) -> dict:
    out: dict = {}
    if "max_indexing_capacity_in_ocu" in value:
        out["maxIndexingCapacityInOCU"] = value["max_indexing_capacity_in_ocu"]
    if "max_search_capacity_in_ocu" in value:
        out["maxSearchCapacityInOCU"] = value["max_search_capacity_in_ocu"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CapacityLimits:
    out: CapacityLimits = {}  # type: ignore[typeddict-item]
    if "maxIndexingCapacityInOCU" in data:
        out["max_indexing_capacity_in_ocu"] = data["maxIndexingCapacityInOCU"]
    if "maxSearchCapacityInOCU" in data:
        out["max_search_capacity_in_ocu"] = data["maxSearchCapacityInOCU"]
    return out
