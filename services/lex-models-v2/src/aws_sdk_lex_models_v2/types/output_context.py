"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#OutputContext``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_lex_models_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_models_v2.types.context_time_to_live_in_seconds
    import aws_sdk_lex_models_v2.types.context_turns_to_live
    import aws_sdk_lex_models_v2.types.name


class OutputContext(TypedDict):
    name: "aws_sdk_lex_models_v2.types.name.Name"
    """<p>The name of the output context.</p>"""
    time_to_live_in_seconds: "aws_sdk_lex_models_v2.types.context_time_to_live_in_seconds.ContextTimeToLiveInSeconds"
    """<p>The amount of time, in seconds, that the output context should remain active. The time is figured from the first time the context is sent to the user.</p>"""
    turns_to_live: (
        "aws_sdk_lex_models_v2.types.context_turns_to_live.ContextTurnsToLive"
    )
    """<p>The number of conversation turns that the output context should remain active. The number of turns is counted from the first time that the context is sent to the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OutputContext) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["timeToLiveInSeconds"] = value["time_to_live_in_seconds"]
    out["turnsToLive"] = value["turns_to_live"]
    return out


def deserialize_json(data: dict) -> OutputContext:
    out: OutputContext = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("OutputContext.name required")
    if "timeToLiveInSeconds" in data:
        out["time_to_live_in_seconds"] = data["timeToLiveInSeconds"]
    else:
        raise DeserializationError("OutputContext.time_to_live_in_seconds required")
    if "turnsToLive" in data:
        out["turns_to_live"] = data["turnsToLive"]
    else:
        raise DeserializationError("OutputContext.turns_to_live required")
    return out
