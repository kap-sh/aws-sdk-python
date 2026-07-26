"""Generated from Smithy shape ``com.amazonaws.wafregional#CreateIPSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.change_token
    import capo_waf_regional.types.ip_set


class CreateIPSetResponse(TypedDict, closed=True):
    ip_set: NotRequired["capo_waf_regional.types.ip_set.IPSet"]
    """<p>The <a>IPSet</a> returned in the <code>CreateIPSet</code> response.</p>"""
    change_token: NotRequired["capo_waf_regional.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateIPSet</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateIPSetResponse) -> dict:
    out: dict = {}
    if "ip_set" in value:
        import capo_waf_regional.types.ip_set

        out["IPSet"] = capo_waf_regional.types.ip_set.serialize_aws_json_1_1(
            value["ip_set"]
        )
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateIPSetResponse:
    out: CreateIPSetResponse = {}  # type: ignore[typeddict-item]
    if "IPSet" in data:
        import capo_waf_regional.types.ip_set

        out["ip_set"] = capo_waf_regional.types.ip_set.deserialize_aws_json_1_1(
            data["IPSet"]
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
