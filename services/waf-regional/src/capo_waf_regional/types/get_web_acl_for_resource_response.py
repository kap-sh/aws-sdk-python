"""Generated from Smithy shape ``com.amazonaws.wafregional#GetWebACLForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.web_acl_summary


class GetWebACLForResourceResponse(TypedDict, closed=True):
    web_acl_summary: NotRequired[
        "capo_waf_regional.types.web_acl_summary.WebACLSummary"
    ]
    """<p>Information about the web ACL that you specified in the <code>GetWebACLForResource</code> request. If there is no associated resource, a null WebACLSummary is returned.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWebACLForResourceResponse) -> dict:
    out: dict = {}
    if "web_acl_summary" in value:
        import capo_waf_regional.types.web_acl_summary

        out["WebACLSummary"] = (
            capo_waf_regional.types.web_acl_summary.serialize_aws_json_1_1(
                value["web_acl_summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWebACLForResourceResponse:
    out: GetWebACLForResourceResponse = {}  # type: ignore[typeddict-item]
    if "WebACLSummary" in data:
        import capo_waf_regional.types.web_acl_summary

        out["web_acl_summary"] = (
            capo_waf_regional.types.web_acl_summary.deserialize_aws_json_1_1(
                data["WebACLSummary"]
            )
        )
    return out
