"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetStageSessionResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.stage_session


class GetStageSessionResponse(TypedDict):
    stage_session: NotRequired["aws_sdk_ivs_realtime.types.stage_session.StageSession"]
    """<p>The stage session that is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStageSessionResponse) -> dict:
    out: dict = {}
    if "stage_session" in value:
        import aws_sdk_ivs_realtime.types.stage_session

        out["stageSession"] = aws_sdk_ivs_realtime.types.stage_session.serialize_json(
            value["stage_session"]
        )
    return out


def deserialize_json(data: dict) -> GetStageSessionResponse:
    out: GetStageSessionResponse = {}  # type: ignore[typeddict-item]
    if "stageSession" in data:
        import aws_sdk_ivs_realtime.types.stage_session

        out["stage_session"] = (
            aws_sdk_ivs_realtime.types.stage_session.deserialize_json(
                data["stageSession"]
            )
        )
    return out
