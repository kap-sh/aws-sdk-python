"""Generated from Smithy shape ``com.amazonaws.wafv2#GetWebACLForResourceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.web_acl


class GetWebACLForResourceResponse(TypedDict, closed=True):
    web_acl: NotRequired["aws_sdk_wafv2.types.web_acl.WebACL"]
    """<p>The web ACL that is associated with the resource. If there is no associated resource, WAF returns a null web ACL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetWebACLForResourceResponse) -> dict:
    out: dict = {}
    if "web_acl" in value:
        import aws_sdk_wafv2.types.web_acl

        out["WebACL"] = aws_sdk_wafv2.types.web_acl.serialize_aws_json_1_1(
            value["web_acl"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetWebACLForResourceResponse:
    out: GetWebACLForResourceResponse = {}  # type: ignore[typeddict-item]
    if "WebACL" in data:
        import aws_sdk_wafv2.types.web_acl

        out["web_acl"] = aws_sdk_wafv2.types.web_acl.deserialize_aws_json_1_1(
            data["WebACL"]
        )
    return out
