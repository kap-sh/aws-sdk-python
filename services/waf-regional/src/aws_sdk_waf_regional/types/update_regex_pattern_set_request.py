"""Generated from Smithy shape ``com.amazonaws.wafregional#UpdateRegexPatternSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_waf_regional.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf_regional.types.change_token
    import aws_sdk_waf_regional.types.regex_pattern_set_updates
    import aws_sdk_waf_regional.types.resource_id


class UpdateRegexPatternSetRequest(TypedDict, closed=True):
    regex_pattern_set_id: "aws_sdk_waf_regional.types.resource_id.ResourceId"
    """<p>The <code>RegexPatternSetId</code> of the <a>RegexPatternSet</a> that you want to update. <code>RegexPatternSetId</code> is returned by <a>CreateRegexPatternSet</a> and by <a>ListRegexPatternSets</a>.</p>"""
    updates: (
        "aws_sdk_waf_regional.types.regex_pattern_set_updates.RegexPatternSetUpdates"
    )
    """<p>An array of <code>RegexPatternSetUpdate</code> objects that you want to insert into or delete from a <a>RegexPatternSet</a>.</p>"""
    change_token: "aws_sdk_waf_regional.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRegexPatternSetRequest) -> dict:
    out: dict = {}
    out["RegexPatternSetId"] = value["regex_pattern_set_id"]
    import aws_sdk_waf_regional.types.regex_pattern_set_updates

    out["Updates"] = (
        aws_sdk_waf_regional.types.regex_pattern_set_updates.serialize_aws_json_1_1(
            value["updates"]
        )
    )
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateRegexPatternSetRequest:
    out: UpdateRegexPatternSetRequest = {}  # type: ignore[typeddict-item]
    if "RegexPatternSetId" in data:
        out["regex_pattern_set_id"] = data["RegexPatternSetId"]
    else:
        raise DeserializationError(
            "UpdateRegexPatternSetRequest.regex_pattern_set_id required"
        )
    if "Updates" in data:
        import aws_sdk_waf_regional.types.regex_pattern_set_updates

        out["updates"] = (
            aws_sdk_waf_regional.types.regex_pattern_set_updates.deserialize_aws_json_1_1(
                data["Updates"]
            )
        )
    else:
        raise DeserializationError("UpdateRegexPatternSetRequest.updates required")
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("UpdateRegexPatternSetRequest.change_token required")
    return out
