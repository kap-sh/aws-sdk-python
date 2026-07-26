"""Generated from Smithy shape ``com.amazonaws.waf#RegexPatternSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_waf.errors import DeserializationError

if TYPE_CHECKING:
    import capo_waf.types.regex_pattern_strings
    import capo_waf.types.resource_id
    import capo_waf.types.resource_name


class RegexPatternSet(TypedDict, closed=True):
    regex_pattern_set_id: "capo_waf.types.resource_id.ResourceId"
    """<p>The identifier for the <code>RegexPatternSet</code>. You use <code>RegexPatternSetId</code> to get information about a <code>RegexPatternSet</code>, update a <code>RegexPatternSet</code>, remove a <code>RegexPatternSet</code> from a <code>RegexMatchSet</code>, and delete a <code>RegexPatternSet</code> from AWS WAF.</p> <p> <code>RegexMatchSetId</code> is returned by <a>CreateRegexPatternSet</a> and by <a>ListRegexPatternSets</a>.</p>"""
    name: NotRequired["capo_waf.types.resource_name.ResourceName"]
    """<p>A friendly name or description of the <a>RegexPatternSet</a>. You can't change <code>Name</code> after you create a <code>RegexPatternSet</code>.</p>"""
    regex_pattern_strings: "capo_waf.types.regex_pattern_strings.RegexPatternStrings"
    """<p>Specifies the regular expression (regex) patterns that you want AWS WAF to search for, such as <code>B[a@]dB[o0]t</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexPatternSet) -> dict:
    out: dict = {}
    out["RegexPatternSetId"] = value["regex_pattern_set_id"]
    if "name" in value:
        out["Name"] = value["name"]
    import capo_waf.types.regex_pattern_strings

    out["RegexPatternStrings"] = (
        capo_waf.types.regex_pattern_strings.serialize_aws_json_1_1(
            value["regex_pattern_strings"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RegexPatternSet:
    out: RegexPatternSet = {}  # type: ignore[typeddict-item]
    if "RegexPatternSetId" in data:
        out["regex_pattern_set_id"] = data["RegexPatternSetId"]
    else:
        raise DeserializationError("RegexPatternSet.regex_pattern_set_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "RegexPatternStrings" in data:
        import capo_waf.types.regex_pattern_strings

        out["regex_pattern_strings"] = (
            capo_waf.types.regex_pattern_strings.deserialize_aws_json_1_1(
                data["RegexPatternStrings"]
            )
        )
    else:
        raise DeserializationError("RegexPatternSet.regex_pattern_strings required")
    return out
