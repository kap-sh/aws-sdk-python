"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DeleteAudienceGenerationJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.audience_generation_job_arn


class DeleteAudienceGenerationJobRequest(TypedDict, closed=True):
    audience_generation_job_arn: (
        "capo_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
    )
    """<p>The Amazon Resource Name (ARN) of the audience generation job that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAudienceGenerationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAudienceGenerationJobRequest:
    out: DeleteAudienceGenerationJobRequest = {}  # type: ignore[typeddict-item]
    return out
