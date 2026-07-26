"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#UpdateStageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.stage


class UpdateStageResponse(TypedDict, closed=True):
    stage: NotRequired["capo_ivs_realtime.types.stage.Stage"]
    """<p>The updated stage.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStageResponse) -> dict:
    out: dict = {}
    if "stage" in value:
        import capo_ivs_realtime.types.stage

        out["stage"] = capo_ivs_realtime.types.stage.serialize_json(value["stage"])
    return out


def deserialize_json(data: dict) -> UpdateStageResponse:
    out: UpdateStageResponse = {}  # type: ignore[typeddict-item]
    if "stage" in data:
        import capo_ivs_realtime.types.stage

        out["stage"] = capo_ivs_realtime.types.stage.deserialize_json(data["stage"])
    return out
