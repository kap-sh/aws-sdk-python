"""Generated from Smithy shape ``com.amazonaws.wafv2#Regex``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_wafv2.types.regex_pattern_string


class Regex(TypedDict, closed=True):
    regex_string: NotRequired[
        "aws_sdk_wafv2.types.regex_pattern_string.RegexPatternString"
    ]
    """<p>The string representing the regular expression.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Regex) -> dict:
    out: dict = {}
    if "regex_string" in value:
        out["RegexString"] = value["regex_string"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Regex:
    out: Regex = {}  # type: ignore[typeddict-item]
    if "RegexString" in data:
        out["regex_string"] = data["RegexString"]
    return out
