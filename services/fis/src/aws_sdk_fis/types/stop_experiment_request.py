"""Generated from Smithy shape ``com.amazonaws.fis#StopExperimentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_id


class StopExperimentRequest(TypedDict):
    id: "aws_sdk_fis.types.experiment_id.ExperimentId"
    """<p>The ID of the experiment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopExperimentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopExperimentRequest:
    out: StopExperimentRequest = {}  # type: ignore[typeddict-item]
    return out
