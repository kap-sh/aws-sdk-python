"""Generated from Smithy shape ``com.amazonaws.wafregional#UpdateWebACLResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.change_token


class UpdateWebACLResponse(TypedDict, closed=True):
    change_token: NotRequired["capo_waf_regional.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>UpdateWebACL</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateWebACLResponse) -> dict:
    out: dict = {}
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateWebACLResponse:
    out: UpdateWebACLResponse = {}  # type: ignore[typeddict-item]
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
