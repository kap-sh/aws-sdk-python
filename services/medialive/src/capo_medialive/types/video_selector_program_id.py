"""Generated from Smithy shape ``com.amazonaws.medialive#VideoSelectorProgramId``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__integer_min0_max65536


class VideoSelectorProgramId(TypedDict, closed=True):
    program_id: NotRequired[
        "capo_medialive.types.__integer_min0_max65536.__integerMin0Max65536"
    ]
    """Selects a specific program from within a multi-program transport stream. If the program doesn't exist, the first program within the transport stream will be selected by default."""


# --- restJson1 ser/de ---
def serialize_json(value: VideoSelectorProgramId) -> dict:
    out: dict = {}
    if "program_id" in value:
        out["programId"] = value["program_id"]
    return out


def deserialize_json(data: dict) -> VideoSelectorProgramId:
    out: VideoSelectorProgramId = {}  # type: ignore[typeddict-item]
    if "programId" in data:
        out["program_id"] = data["programId"]
    return out
