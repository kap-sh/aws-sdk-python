"""Generated from Smithy shape ``com.amazonaws.entityresolution#GetMatchIdOutput``."""

from typing_extensions import NotRequired, TypedDict


class GetMatchIdOutput(TypedDict, closed=True):
    match_id: NotRequired["str"]
    """<p>The unique identifiers for this group of match records.</p>"""
    match_rule: NotRequired["str"]
    """<p>The rule the record matched on.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMatchIdOutput) -> dict:
    out: dict = {}
    if "match_id" in value:
        out["matchId"] = value["match_id"]
    if "match_rule" in value:
        out["matchRule"] = value["match_rule"]
    return out


def deserialize_json(data: dict) -> GetMatchIdOutput:
    out: GetMatchIdOutput = {}  # type: ignore[typeddict-item]
    if "matchId" in data:
        out["match_id"] = data["matchId"]
    if "matchRule" in data:
        out["match_rule"] = data["matchRule"]
    return out
