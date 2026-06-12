"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#UpdateStageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.stage


class UpdateStageResponse(TypedDict):
    stage: NotRequired["aws_sdk_ivs_realtime.types.stage.Stage"]
    """<p>The updated stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStageResponse) -> dict:
    out: dict = {}
    if "stage" in value:
        import aws_sdk_ivs_realtime.types.stage

        out["stage"] = aws_sdk_ivs_realtime.types.stage.serialize_json(value["stage"])
    return out


def deserialize_json(data: dict) -> UpdateStageResponse:
    out: UpdateStageResponse = {}  # type: ignore[typeddict-item]
    if "stage" in data:
        import aws_sdk_ivs_realtime.types.stage

        out["stage"] = aws_sdk_ivs_realtime.types.stage.deserialize_json(data["stage"])
    return out
