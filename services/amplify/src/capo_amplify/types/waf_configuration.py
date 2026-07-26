"""Generated from Smithy shape ``com.amazonaws.amplify#WafConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplify.types.status_reason
    import capo_amplify.types.waf_status
    import capo_amplify.types.web_acl_arn


class WafConfiguration(TypedDict, closed=True):
    web_acl_arn: NotRequired["capo_amplify.types.web_acl_arn.WebAclArn"]
    """<p>The Amazon Resource Name (ARN) for the web ACL associated with an Amplify app.</p>"""
    waf_status: NotRequired["capo_amplify.types.waf_status.WafStatus"]
    """<p>The status of the process to associate or disassociate a web ACL to an Amplify app.</p>"""
    status_reason: NotRequired["capo_amplify.types.status_reason.StatusReason"]
    """<p>The reason for the current status of the Firewall configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WafConfiguration) -> dict:
    out: dict = {}
    if "web_acl_arn" in value:
        out["webAclArn"] = value["web_acl_arn"]
    if "waf_status" in value:
        import capo_amplify.types.waf_status

        out["wafStatus"] = capo_amplify.types.waf_status.serialize_json(
            value["waf_status"]
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> WafConfiguration:
    out: WafConfiguration = {}  # type: ignore[typeddict-item]
    if "webAclArn" in data:
        out["web_acl_arn"] = data["webAclArn"]
    if "wafStatus" in data:
        import capo_amplify.types.waf_status

        out["waf_status"] = capo_amplify.types.waf_status.deserialize_json(
            data["wafStatus"]
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
