"""Generated from Smithy shape ``com.amazonaws.kendra#ExpandConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.integer


class ExpandConfiguration(TypedDict, closed=True):
    max_result_items_to_expand: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>The number of collapsed search result groups to expand. If you set this value to 10, for example, only the first 10 out of 100 result groups will have expand functionality. </p>"""
    max_expanded_results_per_item: NotRequired["capo_kendra.types.integer.Integer"]
    """<p>The number of expanded results to show per collapsed primary document. For instance, if you set this value to 3, then at most 3 results per collapsed group will be displayed.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExpandConfiguration) -> dict:
    out: dict = {}
    if "max_result_items_to_expand" in value:
        out["MaxResultItemsToExpand"] = value["max_result_items_to_expand"]
    if "max_expanded_results_per_item" in value:
        out["MaxExpandedResultsPerItem"] = value["max_expanded_results_per_item"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExpandConfiguration:
    out: ExpandConfiguration = {}  # type: ignore[typeddict-item]
    if "MaxResultItemsToExpand" in data:
        out["max_result_items_to_expand"] = data["MaxResultItemsToExpand"]
    if "MaxExpandedResultsPerItem" in data:
        out["max_expanded_results_per_item"] = data["MaxExpandedResultsPerItem"]
    return out
