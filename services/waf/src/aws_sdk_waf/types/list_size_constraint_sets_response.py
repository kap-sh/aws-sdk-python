"""Generated from Smithy shape ``com.amazonaws.waf#ListSizeConstraintSetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf.types.next_marker
    import aws_sdk_waf.types.size_constraint_set_summaries


class ListSizeConstraintSetsResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_waf.types.next_marker.NextMarker"]
    """<p>If you have more <code>SizeConstraintSet</code> objects than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>SizeConstraintSet</code> objects, submit another <code>ListSizeConstraintSets</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    size_constraint_sets: NotRequired[
        "aws_sdk_waf.types.size_constraint_set_summaries.SizeConstraintSetSummaries"
    ]
    """<p>An array of <a>SizeConstraintSetSummary</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListSizeConstraintSetsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "size_constraint_sets" in value:
        import aws_sdk_waf.types.size_constraint_set_summaries

        out["SizeConstraintSets"] = (
            aws_sdk_waf.types.size_constraint_set_summaries.serialize_aws_json_1_1(
                value["size_constraint_sets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListSizeConstraintSetsResponse:
    out: ListSizeConstraintSetsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "SizeConstraintSets" in data:
        import aws_sdk_waf.types.size_constraint_set_summaries

        out["size_constraint_sets"] = (
            aws_sdk_waf.types.size_constraint_set_summaries.deserialize_aws_json_1_1(
                data["SizeConstraintSets"]
            )
        )
    return out
