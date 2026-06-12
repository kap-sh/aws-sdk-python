"""Generated from Smithy shape ``com.amazonaws.waf#RegexPatternSetUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.change_action
    import aws_sdk_waf.types.regex_pattern_string


class RegexPatternSetUpdate(TypedDict):
    action: "aws_sdk_waf.types.change_action.ChangeAction"
    """<p>Specifies whether to insert or delete a <code>RegexPatternString</code>.</p>"""
    regex_pattern_string: "aws_sdk_waf.types.regex_pattern_string.RegexPatternString"
    """<p>Specifies the regular expression (regex) pattern that you want AWS WAF to search for, such as <code>B[a@]dB[o0]t</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RegexPatternSetUpdate) -> dict:
    out: dict = {}
    import aws_sdk_waf.types.change_action

    out["Action"] = aws_sdk_waf.types.change_action.serialize_aws_json_1_1(
        value["action"]
    )
    out["RegexPatternString"] = value["regex_pattern_string"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RegexPatternSetUpdate:
    out: RegexPatternSetUpdate = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        import aws_sdk_waf.types.change_action

        out["action"] = aws_sdk_waf.types.change_action.deserialize_aws_json_1_1(
            data["Action"]
        )
    else:
        raise DeserializationError("RegexPatternSetUpdate.action required")
    if "RegexPatternString" in data:
        out["regex_pattern_string"] = data["RegexPatternString"]
    else:
        raise DeserializationError(
            "RegexPatternSetUpdate.regex_pattern_string required"
        )
    return out
