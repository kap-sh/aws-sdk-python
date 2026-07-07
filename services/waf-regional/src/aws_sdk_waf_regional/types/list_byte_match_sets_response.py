"""Generated from Smithy shape ``com.amazonaws.wafregional#ListByteMatchSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.byte_match_set_summaries
    import aws_sdk_waf_regional.types.next_marker


class ListByteMatchSetsResponse(TypedDict, closed=True):
    next_marker: NotRequired["aws_sdk_waf_regional.types.next_marker.NextMarker"]
    """<p>If you have more <code>ByteMatchSet</code> objects than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>ByteMatchSet</code> objects, submit another <code>ListByteMatchSets</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    byte_match_sets: NotRequired[
        "aws_sdk_waf_regional.types.byte_match_set_summaries.ByteMatchSetSummaries"
    ]
    """<p>An array of <a>ByteMatchSetSummary</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListByteMatchSetsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "byte_match_sets" in value:
        import aws_sdk_waf_regional.types.byte_match_set_summaries

        out["ByteMatchSets"] = (
            aws_sdk_waf_regional.types.byte_match_set_summaries.serialize_aws_json_1_1(
                value["byte_match_sets"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListByteMatchSetsResponse:
    out: ListByteMatchSetsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "ByteMatchSets" in data:
        import aws_sdk_waf_regional.types.byte_match_set_summaries

        out["byte_match_sets"] = (
            aws_sdk_waf_regional.types.byte_match_set_summaries.deserialize_aws_json_1_1(
                data["ByteMatchSets"]
            )
        )
    return out
