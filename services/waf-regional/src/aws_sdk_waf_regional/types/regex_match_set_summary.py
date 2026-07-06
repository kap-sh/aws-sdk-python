"""Generated from Smithy shape ``com.amazonaws.wafregional#RegexMatchSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.resource_id
    import aws_sdk_waf_regional.types.resource_name


class RegexMatchSetSummary(TypedDict, closed=True):
    regex_match_set_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>RegexMatchSetId</code> for a <code>RegexMatchSet</code>. You use <code>RegexMatchSetId</code> to get information about a <code>RegexMatchSet</code>, update a <code>RegexMatchSet</code>, remove a <code>RegexMatchSet</code> from a <code>Rule</code>, and delete a <code>RegexMatchSet</code> from AWS WAF.</p> <p> <code>RegexMatchSetId</code> is returned by <a>CreateRegexMatchSet</a> and by <a>ListRegexMatchSets</a>.</p>"""
    name: "aws_sdk_waf_regional.types.resource_name.ResourceName"
    """<p>A friendly name or description of the <a>RegexMatchSet</a>. You can't change <code>Name</code> after you create a <code>RegexMatchSet</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexMatchSetSummary) -> dict:
    out: dict = {}
    out["RegexMatchSetId"] = value["regex_match_set_id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegexMatchSetSummary:
    out: RegexMatchSetSummary = {}  # type: ignore[typeddict-item]
    if "RegexMatchSetId" in data:
        out["regex_match_set_id"] = data["RegexMatchSetId"]
    else:
        raise DeserializationError("RegexMatchSetSummary.regex_match_set_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("RegexMatchSetSummary.name required")
    return out
