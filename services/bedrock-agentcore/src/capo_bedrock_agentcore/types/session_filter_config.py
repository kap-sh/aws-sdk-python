"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#SessionFilterConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime


class SessionFilterConfig(TypedDict, closed=True):
    start_time: NotRequired["datetime.datetime"]
    """<p>The start time of the time range. Only sessions with activity at or after this timestamp are included.</p>"""
    end_time: NotRequired["datetime.datetime"]
    """<p>The end time of the time range. Only sessions with activity before this timestamp are included.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionFilterConfig) -> dict:
    out: dict = {}
    if "start_time" in value:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["startTime"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["endTime"] = capo_bedrock_agentcore.types._prelude.timestamp.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> SessionFilterConfig:
    out: SessionFilterConfig = {}  # type: ignore[typeddict-item]
    if "startTime" in data:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["start_time"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import capo_bedrock_agentcore.types._prelude.timestamp

        out["end_time"] = (
            capo_bedrock_agentcore.types._prelude.timestamp.deserialize_json(
                data["endTime"]
            )
        )
    return out
