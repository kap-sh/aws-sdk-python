"""Generated from Smithy shape ``com.amazonaws.wafv2#CreateRegexPatternSetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wafv2.types.regex_pattern_set_summary


class CreateRegexPatternSetResponse(TypedDict, closed=True):
    summary: NotRequired[
        "capo_wafv2.types.regex_pattern_set_summary.RegexPatternSetSummary"
    ]
    """<p>High-level information about a <a>RegexPatternSet</a>, returned by operations like create and list. This provides information like the ID, that you can use to retrieve and manage a <code>RegexPatternSet</code>, and the ARN, that you provide to the <a>RegexPatternSetReferenceStatement</a> to use the pattern set in a <a>Rule</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRegexPatternSetResponse) -> dict:
    out: dict = {}
    if "summary" in value:
        import capo_wafv2.types.regex_pattern_set_summary

        out["Summary"] = (
            capo_wafv2.types.regex_pattern_set_summary.serialize_aws_json_1_1(
                value["summary"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRegexPatternSetResponse:
    out: CreateRegexPatternSetResponse = {}  # type: ignore[typeddict-item]
    if "Summary" in data:
        import capo_wafv2.types.regex_pattern_set_summary

        out["summary"] = (
            capo_wafv2.types.regex_pattern_set_summary.deserialize_aws_json_1_1(
                data["Summary"]
            )
        )
    return out
