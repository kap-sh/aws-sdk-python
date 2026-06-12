"""Generated from Smithy shape ``com.amazonaws.waf#CreateRegexPatternSetResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_waf.types.change_token
    import aws_sdk_waf.types.regex_pattern_set


class CreateRegexPatternSetResponse(TypedDict):
    regex_pattern_set: NotRequired[
        "aws_sdk_waf.types.regex_pattern_set.RegexPatternSet"
    ]
    """<p>A <a>RegexPatternSet</a> that contains no objects.</p>"""
    change_token: NotRequired["aws_sdk_waf.types.change_token.ChangeToken"]
    """<p>The <code>ChangeToken</code> that you used to submit the <code>CreateRegexPatternSet</code> request. You can also use this value to query the status of the request. For more information, see <a>GetChangeTokenStatus</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRegexPatternSetResponse) -> dict:
    out: dict = {}
    if "regex_pattern_set" in value:
        import aws_sdk_waf.types.regex_pattern_set

        out["RegexPatternSet"] = (
            aws_sdk_waf.types.regex_pattern_set.serialize_aws_json_1_1(
                value["regex_pattern_set"]
            )
        )
    if "change_token" in value:
        out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRegexPatternSetResponse:
    out: CreateRegexPatternSetResponse = {}  # type: ignore[typeddict-item]
    if "RegexPatternSet" in data:
        import aws_sdk_waf.types.regex_pattern_set

        out["regex_pattern_set"] = (
            aws_sdk_waf.types.regex_pattern_set.deserialize_aws_json_1_1(
                data["RegexPatternSet"]
            )
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    return out
