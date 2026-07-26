"""Generated from Smithy shape ``com.amazonaws.medialive#PipelineLockingSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medialive.types.__string
    import capo_medialive.types.pipeline_locking_method


class PipelineLockingSettings(TypedDict, closed=True):
    pipeline_locking_method: NotRequired[
        "capo_medialive.types.pipeline_locking_method.PipelineLockingMethod"
    ]
    """The method to use to lock the video frames in the pipelines. sourceTimecode (default): Use the timecode in the source. videoAlignment: Lock frames that the encoder identifies as having matching content. If videoAlignment is selected, existing timecodes will not be used for any locking decisions."""
    custom_epoch: NotRequired["capo_medialive.types.__string.__string"]
    """Optional. Only applies to CMAF Ingest Output Group and MediaPackage V2 Output Group Only. Enter a value here to use a custom epoch, instead of the standard epoch (which started at 1970-01-01T00:00:00 UTC). Specify the start time of the custom epoch, in YYYY-MM-DDTHH:MM:SS in UTC. The time must be 2000-01-01T00:00:00 or later. Always set the MM:SS portion to 00:00."""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineLockingSettings) -> dict:
    out: dict = {}
    if "pipeline_locking_method" in value:
        import capo_medialive.types.pipeline_locking_method

        out["pipelineLockingMethod"] = (
            capo_medialive.types.pipeline_locking_method.serialize_json(
                value["pipeline_locking_method"]
            )
        )
    if "custom_epoch" in value:
        out["customEpoch"] = value["custom_epoch"]
    return out


def deserialize_json(data: dict) -> PipelineLockingSettings:
    out: PipelineLockingSettings = {}  # type: ignore[typeddict-item]
    if "pipelineLockingMethod" in data:
        import capo_medialive.types.pipeline_locking_method

        out["pipeline_locking_method"] = (
            capo_medialive.types.pipeline_locking_method.deserialize_json(
                data["pipelineLockingMethod"]
            )
        )
    if "customEpoch" in data:
        out["custom_epoch"] = data["customEpoch"]
    return out
