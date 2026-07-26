"""Generated from Smithy shape ``com.amazonaws.fis#StopExperimentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment_id


class StopExperimentRequest(TypedDict, closed=True):
    id: "capo_fis.types.experiment_id.ExperimentId"
    """<p>The ID of the experiment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopExperimentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopExperimentRequest:
    out: StopExperimentRequest = {}  # type: ignore[typeddict-item]
    return out
