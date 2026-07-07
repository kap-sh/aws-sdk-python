"""Generated from Smithy shape ``com.amazonaws.wafregional#GetXssMatchSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.xss_match_set


class GetXssMatchSetResponse(TypedDict, closed=True):
    xss_match_set: NotRequired["aws_sdk_waf_regional.types.xss_match_set.XssMatchSet"]
    """<p>Information about the <a>XssMatchSet</a> that you specified in the <code>GetXssMatchSet</code> request. For more information, see the following topics:</p> <ul> <li> <p> <a>XssMatchSet</a>: Contains <code>Name</code>, <code>XssMatchSetId</code>, and an array of <code>XssMatchTuple</code> objects</p> </li> <li> <p> <a>XssMatchTuple</a>: Each <code>XssMatchTuple</code> object contains <code>FieldToMatch</code> and <code>TextTransformation</code> </p> </li> <li> <p> <a>FieldToMatch</a>: Contains <code>Data</code> and <code>Type</code> </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetXssMatchSetResponse) -> dict:
    out: dict = {}
    if "xss_match_set" in value:
        import aws_sdk_waf_regional.types.xss_match_set

        out["XssMatchSet"] = (
            aws_sdk_waf_regional.types.xss_match_set.serialize_aws_json_1_1(
                value["xss_match_set"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetXssMatchSetResponse:
    out: GetXssMatchSetResponse = {}  # type: ignore[typeddict-item]
    if "XssMatchSet" in data:
        import aws_sdk_waf_regional.types.xss_match_set

        out["xss_match_set"] = (
            aws_sdk_waf_regional.types.xss_match_set.deserialize_aws_json_1_1(
                data["XssMatchSet"]
            )
        )
    return out
