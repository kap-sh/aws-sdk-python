"""Generated from Smithy shape ``com.amazonaws.waf#DeleteRegexPatternSetRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_waf.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_waf.types.change_token
    import aws_sdk_waf.types.resource_id


class DeleteRegexPatternSetRequest(TypedDict):
    regex_pattern_set_id: "aws_sdk_waf.types.resource_id.ResourceId"
    """<p>The <code>RegexPatternSetId</code> of the <a>RegexPatternSet</a> that you want to delete. <code>RegexPatternSetId</code> is returned by <a>CreateRegexPatternSet</a> and by <a>ListRegexPatternSets</a>.</p>"""
    change_token: "aws_sdk_waf.types.change_token.ChangeToken"
    """<p>The value returned by the most recent call to <a>GetChangeToken</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteRegexPatternSetRequest) -> dict:
    out: dict = {}
    out["RegexPatternSetId"] = value["regex_pattern_set_id"]
    out["ChangeToken"] = value["change_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteRegexPatternSetRequest:
    out: DeleteRegexPatternSetRequest = {}  # type: ignore[typeddict-item]
    if "RegexPatternSetId" in data:
        out["regex_pattern_set_id"] = data["RegexPatternSetId"]
    else:
        raise DeserializationError(
            "DeleteRegexPatternSetRequest.regex_pattern_set_id required"
        )
    if "ChangeToken" in data:
        out["change_token"] = data["ChangeToken"]
    else:
        raise DeserializationError("DeleteRegexPatternSetRequest.change_token required")
    return out
