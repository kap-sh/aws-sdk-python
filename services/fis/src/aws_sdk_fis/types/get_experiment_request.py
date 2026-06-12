"""Generated from Smithy shape ``com.amazonaws.fis#GetExperimentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_id


class GetExperimentRequest(TypedDict):
    id: "aws_sdk_fis.types.experiment_id.ExperimentId"
    """<p>The ID of the experiment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetExperimentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetExperimentRequest:
    out: GetExperimentRequest = {}  # type: ignore[typeddict-item]
    return out
