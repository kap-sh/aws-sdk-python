"""Generated from Smithy shape ``com.amazonaws.waf#ListIPSetsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf.types.ip_set_summaries
    import aws_sdk_waf.types.next_marker


class ListIPSetsResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_waf.types.next_marker.NextMarker"]
    """<p>To list more <code>IPSet</code> objects, submit another <code>ListIPSets</code> request, and in the next request use the <code>NextMarker</code> response value as the <code>NextMarker</code> value.</p>"""
    ip_sets: NotRequired["aws_sdk_waf.types.ip_set_summaries.IPSetSummaries"]
    """<p>An array of <a>IPSetSummary</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListIPSetsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "ip_sets" in value:
        import aws_sdk_waf.types.ip_set_summaries

        out["IPSets"] = aws_sdk_waf.types.ip_set_summaries.serialize_aws_json_1_1(
            value["ip_sets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListIPSetsResponse:
    out: ListIPSetsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "IPSets" in data:
        import aws_sdk_waf.types.ip_set_summaries

        out["ip_sets"] = aws_sdk_waf.types.ip_set_summaries.deserialize_aws_json_1_1(
            data["IPSets"]
        )
    return out
