"""Generated from Smithy shape ``com.amazonaws.fis#StartExperimentResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fis.types.experiment


class StartExperimentResponse(TypedDict, closed=True):
    experiment: NotRequired["capo_fis.types.experiment.Experiment"]
    """<p>Information about the experiment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartExperimentResponse) -> dict:
    out: dict = {}
    if "experiment" in value:
        import capo_fis.types.experiment

        out["experiment"] = capo_fis.types.experiment.serialize_json(
            value["experiment"]
        )
    return out


def deserialize_json(data: dict) -> StartExperimentResponse:
    out: StartExperimentResponse = {}  # type: ignore[typeddict-item]
    if "experiment" in data:
        import capo_fis.types.experiment

        out["experiment"] = capo_fis.types.experiment.deserialize_json(
            data["experiment"]
        )
    return out
