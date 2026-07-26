"""Generated from Smithy shape ``com.amazonaws.wafregional#UpdateXssMatchSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf_regional.types.change_token
    import capo_waf_regional.types.resource_id
    import capo_waf_regional.types.xss_match_set_updates


class UpdateXssMatchSetRequest(TypedDict, closed=True):
    xss_match_set_id: "capo_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>XssMatchSetId</code> of the <code>XssMatchSet</code> that you want to update. <code>XssMatchSetId</code> is returned by <a>CreateXssMatchSet</a> and by <a>ListXssMatchSets</a>.</p>"""
    change_token: "capo_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""
    updates: "capo_waf_regional.types.xss_match_set_updates.XssMatchSetUpdates"
    """<p>An array of <code>XssMatchSetUpdate</code> objects that you want to insert into or delete from an <a>XssMatchSet</a>. For more information, see the applicable data types:</p> <ul> <li> <p> <a>XssMatchSetUpdate</a>: Contains <code>Action</code> and <code>XssMatchTuple</code> </p> </li> <li> <p> <a>XssMatchTuple</a>: Contains <code>FieldToMatch</code> and <code>TextTransformation</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateXssMatchSetRequest) -> dict:
    out: dict = {}
    out["XssMatchSetId"] = value["xss_match_set_id"]
    out["ChangeToken"] = value["change_token"]
    import capo_waf_regional.types.xss_match_set_updates

    out["Updates"] = (
        capo_waf_regional.types.xss_match_set_updates.serialize_aws_json_1_1(
            value["updates"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateXssMatchSetRequest:
    out: UpdateXssMatchSetRequest = {}  # type: ignore[typeddict-item]
    if "XssMatchSetId" in data:
        out["xss_match_set_id"] = data["XssMatchSetId"]
    else:
        raise DeserializationError("UpdateXssMatchSetRequest.xss_match_set_id required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("UpdateXssMatchSetRequest.change_token required")
    if "Updates" in data:
        import capo_waf_regional.types.xss_match_set_updates

        out["updates"] = (
            capo_waf_regional.types.xss_match_set_updates.deserialize_aws_json_1_1(
                data["Updates"]
            )
        )
    else:
        raise DeserializationError("UpdateXssMatchSetRequest.updates required")
    return out
