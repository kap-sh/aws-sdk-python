"""Generated from Smithy shape ``com.amazonaws.wafregional#GetRegexPatternSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.regex_pattern_set


class GetRegexPatternSetResponse(TypedDict, closed=True):
    regex_pattern_set: NotRequired[
        "aws_sdk_waf_regional.types.regex_pattern_set.RegexPatternSet"
    ]
    """<p>Information about the <a>RegexPatternSet</a> that you specified in the <code>GetRegexPatternSet</code> request, including the identifier of the pattern set and the regular expression patterns you want AWS WAF to search for. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRegexPatternSetResponse) -> dict:
    out: dict = {}
    if "regex_pattern_set" in value:
        import aws_sdk_waf_regional.types.regex_pattern_set

        out["RegexPatternSet"] = (
            aws_sdk_waf_regional.types.regex_pattern_set.serialize_aws_json_1_1(
                value["regex_pattern_set"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRegexPatternSetResponse:
    out: GetRegexPatternSetResponse = {}  # type: ignore[typeddict-item]
    if "RegexPatternSet" in data:
        import aws_sdk_waf_regional.types.regex_pattern_set

        out["regex_pattern_set"] = (
            aws_sdk_waf_regional.types.regex_pattern_set.deserialize_aws_json_1_1(
                data["RegexPatternSet"]
            )
        )
    return out
