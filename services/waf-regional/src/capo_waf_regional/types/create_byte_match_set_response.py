"""Generated from Smithy shape ``com.amazonaws.wafregional#CreateByteMatchSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_waf_regional.types.byte_match_set
    import capo_waf_regional.types.change_token


class CreateByteMatchSetResponse(TypedDict, closed=True):
    byte_match_set: NotRequired["capo_waf_regional.types.byte_match_set.ByteMatchSet"]
    """<p>A <a>ByteMatchSet</a> that contains no <code>ByteMatchTuple</code> objects.</p>"""
    change_token: NotRequired["capo_waf_regional.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateByteMatchSet</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateByteMatchSetResponse) -> dict:
    out: dict = {}
    if "byte_match_set" in value:
        import capo_waf_regional.types.byte_match_set

        out["ByteMatchSet"] = (
            capo_waf_regional.types.byte_match_set.serialize_aws_json_1_1(
                value["byte_match_set"]
            )
        )
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateByteMatchSetResponse:
    out: CreateByteMatchSetResponse = {}  # type: ignore[typeddict-item]
    if "ByteMatchSet" in data:
        import capo_waf_regional.types.byte_match_set

        out["byte_match_set"] = (
            capo_waf_regional.types.byte_match_set.deserialize_aws_json_1_1(
                data["ByteMatchSet"]
            )
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
