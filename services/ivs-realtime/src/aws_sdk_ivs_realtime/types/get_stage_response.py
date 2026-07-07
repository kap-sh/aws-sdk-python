"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetStageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.stage


class GetStageResponse(TypedDict, closed=True):
    stage: NotRequired["aws_sdk_ivs_realtime.types.stage.Stage"]
    """<p>The stage that is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetStageResponse) -> dict:
    out: dict = {}
    if "stage" in value:
        import aws_sdk_ivs_realtime.types.stage

        out["stage"] = aws_sdk_ivs_realtime.types.stage.serialize_json(value["stage"])
    return out


def deserialize_json(data: dict) -> GetStageResponse:
    out: GetStageResponse = {}  # type: ignore[typeddict-item]
    if "stage" in data:
        import aws_sdk_ivs_realtime.types.stage

        out["stage"] = aws_sdk_ivs_realtime.types.stage.deserialize_json(data["stage"])
    return out
