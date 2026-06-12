"""Generated from Smithy shape ``com.amazonaws.wafregional#RegexMatchSet``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.regex_match_tuples
    import aws_sdk_waf_regional.types.resource_id
    import aws_sdk_waf_regional.types.resource_name


class RegexMatchSet(TypedDict):
    regex_match_set_id: NotRequired["aws_sdk_waf_regional.types.resource_id.ResourceId"]
    """<p>The <code>RegexMatchSetId</code> for a <code>RegexMatchSet</code>. You use <code>RegexMatchSetId</code> to get information about a <code>RegexMatchSet</code> (see <a>GetRegexMatchSet</a>), update a <code>RegexMatchSet</code> (see <a>UpdateRegexMatchSet</a>), insert a <code>RegexMatchSet</code> into a <code>Rule</code> or delete one from a <code>Rule</code> (see <a>UpdateRule</a>), and delete a <code>RegexMatchSet</code> from AWS WAF (see <a>DeleteRegexMatchSet</a>).</p> <p> <code>RegexMatchSetId</code> is returned by <a>CreateRegexMatchSet</a> and by <a>ListRegexMatchSets</a>.</p>"""
    name: NotRequired["aws_sdk_waf_regional.types.resource_name.ResourceName"]
    """<p>A friendly name or description of the <a>RegexMatchSet</a>. You can't change <code>Name</code> after you create a <code>RegexMatchSet</code>.</p>"""
    regex_match_tuples: NotRequired[
        "aws_sdk_waf_regional.types.regex_match_tuples.RegexMatchTuples"
    ]
    """<p>Contains an array of <a>RegexMatchTuple</a> objects. Each <code>RegexMatchTuple</code> object contains: </p> <ul> <li> <p>The part of a web request that you want AWS WAF to inspect, such as a query string or the value of the <code>User-Agent</code> header. </p> </li> <li> <p>The identifier of the pattern (a regular expression) that you want AWS WAF to look for. For more information, see <a>RegexPatternSet</a>.</p> </li> <li> <p>Whether to perform any conversions on the request, such as converting it to lowercase, before inspecting it for the specified string.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexMatchSet) -> dict:
    out: dict = {}
    if "regex_match_set_id" in value:
        out["RegexMatchSetId"] = value["regex_match_set_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "regex_match_tuples" in value:
        import aws_sdk_waf_regional.types.regex_match_tuples

        out["RegexMatchTuples"] = (
            aws_sdk_waf_regional.types.regex_match_tuples.serialize_aws_json_1_1(
                value["regex_match_tuples"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegexMatchSet:
    out: RegexMatchSet = {}  # type: ignore[typeddict-item]
    if "RegexMatchSetId" in data:
        out["regex_match_set_id"] = data["RegexMatchSetId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "RegexMatchTuples" in data:
        import aws_sdk_waf_regional.types.regex_match_tuples

        out["regex_match_tuples"] = (
            aws_sdk_waf_regional.types.regex_match_tuples.deserialize_aws_json_1_1(
                data["RegexMatchTuples"]
            )
        )
    return out
