"""Generated from Smithy shape ``com.amazonaws.lexruntimeservice#ActiveContextTimeToLive``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_lex_runtime_service.types.active_context_time_to_live_in_seconds
    import aws_sdk_lex_runtime_service.types.active_context_turns_to_live


class ActiveContextTimeToLive(TypedDict, closed=True):
    time_to_live_in_seconds: NotRequired[
        "aws_sdk_lex_runtime_service.types.active_context_time_to_live_in_seconds.ActiveContextTimeToLiveInSeconds"
    ]
    """<p>The number of seconds that the context should be active after it is first sent in a <code>PostContent</code> or <code>PostText</code> response. You can set the value between 5 and 86,400 seconds (24 hours).</p>"""
    turns_to_live: NotRequired[
        "aws_sdk_lex_runtime_service.types.active_context_turns_to_live.ActiveContextTurnsToLive"
    ]
    """<p>The number of conversation turns that the context should be active. A conversation turn is one <code>PostContent</code> or <code>PostText</code> request and the corresponding response from Amazon Lex.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActiveContextTimeToLive) -> dict:
    out: dict = {}
    if "time_to_live_in_seconds" in value:
        out["timeToLiveInSeconds"] = value["time_to_live_in_seconds"]
    if "turns_to_live" in value:
        out["turnsToLive"] = value["turns_to_live"]
    return out


def deserialize_json(data: dict) -> ActiveContextTimeToLive:
    out: ActiveContextTimeToLive = {}  # type: ignore[typeddict-item]
    if "timeToLiveInSeconds" in data:
        out["time_to_live_in_seconds"] = data["timeToLiveInSeconds"]
    if "turnsToLive" in data:
        out["turns_to_live"] = data["turnsToLive"]
    return out
