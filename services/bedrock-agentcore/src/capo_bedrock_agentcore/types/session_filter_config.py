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
        import capo_bedrock_agentcore._protocol.serialize

        out["startTime"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
            value["start_time"]
        )
    if "end_time" in value:
        import capo_bedrock_agentcore._protocol.serialize

        out["endTime"] = capo_bedrock_agentcore._protocol.serialize.fmt_date_time(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> SessionFilterConfig:
    out: SessionFilterConfig = {}  # type: ignore[typeddict-item]
    if data.get("startTime") is not None:
        import datetime

        out["start_time"] = datetime.datetime.fromisoformat(
            data["startTime"].replace("Z", "+00:00")
        )
    if data.get("endTime") is not None:
        import datetime

        out["end_time"] = datetime.datetime.fromisoformat(
            data["endTime"].replace("Z", "+00:00")
        )
    return out
