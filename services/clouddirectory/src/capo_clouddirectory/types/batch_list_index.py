"""Generated from Smithy shape ``com.amazonaws.clouddirectory#BatchListIndex``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.next_token
    import capo_clouddirectory.types.number_results
    import capo_clouddirectory.types.object_attribute_range_list
    import capo_clouddirectory.types.object_reference


class BatchListIndex(TypedDict, closed=True):
    ranges_on_indexed_values: NotRequired[
        "capo_clouddirectory.types.object_attribute_range_list.ObjectAttributeRangeList"
    ]
    """<p>Specifies the ranges of indexed values that you want to query.</p>"""
    index_reference: "capo_clouddirectory.types.object_reference.ObjectReference"
    """<p>The reference to the index to list.</p>"""
    max_results: NotRequired["capo_clouddirectory.types.number_results.NumberResults"]
    """<p>The maximum number of results to retrieve.</p>"""
    next_token: NotRequired["capo_clouddirectory.types.next_token.NextToken"]
    """<p>The pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchListIndex) -> dict:
    out: dict = {}
    if "ranges_on_indexed_values" in value:
        import capo_clouddirectory.types.object_attribute_range_list

        out["RangesOnIndexedValues"] = (
            capo_clouddirectory.types.object_attribute_range_list.serialize_json(
                value["ranges_on_indexed_values"]
            )
        )
    import capo_clouddirectory.types.object_reference

    out["IndexReference"] = capo_clouddirectory.types.object_reference.serialize_json(
        value["index_reference"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> BatchListIndex:
    out: BatchListIndex = {}  # type: ignore[typeddict-item]
    if "RangesOnIndexedValues" in data:
        import capo_clouddirectory.types.object_attribute_range_list

        out["ranges_on_indexed_values"] = (
            capo_clouddirectory.types.object_attribute_range_list.deserialize_json(
                data["RangesOnIndexedValues"]
            )
        )
    if "IndexReference" in data:
        import capo_clouddirectory.types.object_reference

        out["index_reference"] = (
            capo_clouddirectory.types.object_reference.deserialize_json(
                data["IndexReference"]
            )
        )
    else:
        raise DeserializationError("BatchListIndex.index_reference required")
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
