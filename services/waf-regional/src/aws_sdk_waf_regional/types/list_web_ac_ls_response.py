"""Generated from Smithy shape ``com.amazonaws.wafregional#ListWebACLsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.next_marker
    import aws_sdk_waf_regional.types.web_acl_summaries


class ListWebACLsResponse(TypedDict):
    next_marker: NotRequired["aws_sdk_waf_regional.types.next_marker.NextMarker"]
    """<p>If you have more <code>WebACL</code> objects than the number that you specified for <code>Limit</code> in the request, the response includes a <code>NextMarker</code> value. To list more <code>WebACL</code> objects, submit another <code>ListWebACLs</code> request, and specify the <code>NextMarker</code> value from the response in the <code>NextMarker</code> value in the next request.</p>"""
    web_ac_ls: NotRequired[
        "aws_sdk_waf_regional.types.web_acl_summaries.WebACLSummaries"
    ]
    """<p>An array of <a>WebACLSummary</a> objects.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListWebACLsResponse) -> dict:
    out: dict = {}
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    if "web_ac_ls" in value:
        import aws_sdk_waf_regional.types.web_acl_summaries

        out["WebACLs"] = (
            aws_sdk_waf_regional.types.web_acl_summaries.serialize_aws_json_1_1(
                value["web_ac_ls"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListWebACLsResponse:
    out: ListWebACLsResponse = {}  # type: ignore[typeddict-item]
    if "NextMarker" in data:
        out["next_marker"] = data["NextMarker"]
    if "WebACLs" in data:
        import aws_sdk_waf_regional.types.web_acl_summaries

        out["web_ac_ls"] = (
            aws_sdk_waf_regional.types.web_acl_summaries.deserialize_aws_json_1_1(
                data["WebACLs"]
            )
        )
    return out
