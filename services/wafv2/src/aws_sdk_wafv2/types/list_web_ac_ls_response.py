"""Generated from Smithy shape ``com.amazonaws.wafv2#ListWebACLsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.next_marker
    import aws_sdk_wafv2.types.web_acl_summaries


class ListWebACLsResponse(TypedDict, closed=True):
    next_marker: NotRequired["aws_sdk_wafv2.types.next_marker.NextMarker"]
    """<p>When you request a list of objects with a <code>Limit</code> setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a <code>NextMarker</code> value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.</p>"""
    web_ac_ls: NotRequired["aws_sdk_wafv2.types.web_acl_summaries.WebACLSummaries"]
    """<p>Array of web ACLs. If you specified a <code>Limit</code> in your request, this might not be the full list. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWebACLsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "web_ac_ls" in value:
        import aws_sdk_wafv2.types.web_acl_summaries

        out["WebACLs"] = aws_sdk_wafv2.types.web_acl_summaries.serialize_aws_json_1_1(
            value["web_ac_ls"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWebACLsResponse:
    out: ListWebACLsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "WebACLs" in data:
        import aws_sdk_wafv2.types.web_acl_summaries

        out["web_ac_ls"] = (
            aws_sdk_wafv2.types.web_acl_summaries.deserialize_aws_json_1_1(
                data["WebACLs"]
            )
        )
    return out
