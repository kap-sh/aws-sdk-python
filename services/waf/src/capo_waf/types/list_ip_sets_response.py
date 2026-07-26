"""Generated from Smithy shape ``com.amazonaws.waf#ListIPSetsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf.types.ip_set_summaries
    import capo_waf.types.next_marker


class ListIPSetsResponse(TypedDict, closed=True):
    next_marker: NotRequired["capo_waf.types.next_marker.NextMarker"]
    """<p>To list more <code>IPSet</code> objects, submit another <code>ListIPSets</code> request, and in the next request use the <code>NextMarker</code> response value as the <code>NextMarker</code> value.</p>"""
    ip_sets: NotRequired["capo_waf.types.ip_set_summaries.IPSetSummaries"]
    """<p>An array of <a>IPSetSummary</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIPSetsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "ip_sets" in value:
        import capo_waf.types.ip_set_summaries

        out["IPSets"] = capo_waf.types.ip_set_summaries.serialize_aws_json_1_1(
            value["ip_sets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIPSetsResponse:
    out: ListIPSetsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "IPSets" in data:
        import capo_waf.types.ip_set_summaries

        out["ip_sets"] = capo_waf.types.ip_set_summaries.deserialize_aws_json_1_1(
            data["IPSets"]
        )
    return out
