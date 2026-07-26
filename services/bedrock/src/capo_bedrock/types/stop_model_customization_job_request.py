"""Generated from Smithy shape ``com.amazonaws.bedrock#StopModelCustomizationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.model_customization_job_identifier


class StopModelCustomizationJobRequest(TypedDict, closed=True):
    job_identifier: "capo_bedrock.types.model_customization_job_identifier.ModelCustomizationJobIdentifier"
    """<p>Job identifier of the job to stop.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopModelCustomizationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopModelCustomizationJobRequest:
    out: StopModelCustomizationJobRequest = {}  # type: ignore[typeddict-item]
    return out
