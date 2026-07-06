"""Generated from Smithy shape ``com.amazonaws.wafregional#CreateWebACLResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_token
    import aws_sdk_waf_regional.types.web_acl


class CreateWebACLResponse(TypedDict, closed=True):
    web_acl: NotRequired["aws_sdk_waf_regional.types.web_acl.WebACL"]
    """<p>The <a>WebACL</a> returned in the <code>CreateWebACL</code> response.</p>"""
    change_token: NotRequired["aws_sdk_waf_regional.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateWebACL</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWebACLResponse) -> dict:
    out: dict = {}
    if "web_acl" in value:
        import aws_sdk_waf_regional.types.web_acl

        out["WebACL"] = aws_sdk_waf_regional.types.web_acl.serialize_aws_json_1_1(
            value["web_acl"]
        )
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWebACLResponse:
    out: CreateWebACLResponse = {}  # type: ignore[typeddict-item]
    if "WebACL" in data:
        import aws_sdk_waf_regional.types.web_acl

        out["web_acl"] = aws_sdk_waf_regional.types.web_acl.deserialize_aws_json_1_1(
            data["WebACL"]
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
