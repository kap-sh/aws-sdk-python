"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#StageSession``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.stage_session_id
    import aws_sdk_ivs_realtime.types.time


class StageSession(TypedDict, closed=True):
    session_id: NotRequired[
        "aws_sdk_ivs_realtime.types.stage_session_id.StageSessionId"
    ]
    """<p>ID of the session within the stage.</p>"""
    start_time: NotRequired["aws_sdk_ivs_realtime.types.time.Time"]
    """<p> ISO 8601 timestamp (returned as a string) when this stage session began.</p>"""
    end_time: NotRequired["aws_sdk_ivs_realtime.types.time.Time"]
    """<p>ISO 8601 timestamp (returned as a string) when the stage session ended. This is null if the stage is active.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StageSession) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["sessionId"] = value["session_id"]
    if "start_time" in value:
        import aws_sdk_ivs_realtime.types.time

        out["startTime"] = aws_sdk_ivs_realtime.types.time.serialize_json(
            value["start_time"]
        )
    if "end_time" in value:
        import aws_sdk_ivs_realtime.types.time

        out["endTime"] = aws_sdk_ivs_realtime.types.time.serialize_json(
            value["end_time"]
        )
    return out


def deserialize_json(data: dict) -> StageSession:
    out: StageSession = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    if "startTime" in data:
        import aws_sdk_ivs_realtime.types.time

        out["start_time"] = aws_sdk_ivs_realtime.types.time.deserialize_json(
            data["startTime"]
        )
    if "endTime" in data:
        import aws_sdk_ivs_realtime.types.time

        out["end_time"] = aws_sdk_ivs_realtime.types.time.deserialize_json(
            data["endTime"]
        )
    return out
