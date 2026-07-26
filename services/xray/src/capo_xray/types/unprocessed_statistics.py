"""Generated from Smithy shape ``com.amazonaws.xray#UnprocessedStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.string


class UnprocessedStatistics(TypedDict, closed=True):
    rule_name: NotRequired["capo_xray.types.string.String"]
    """<p>The name of the sampling rule.</p>"""
    error_code: NotRequired["capo_xray.types.string.String"]
    """<p>The error code.</p>"""
    message: NotRequired["capo_xray.types.string.String"]
    """<p>The error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedStatistics) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_json(data: dict) -> UnprocessedStatistics:
    out: UnprocessedStatistics = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "Message" in data:
        out["message"] = data["Message"]
    return out
