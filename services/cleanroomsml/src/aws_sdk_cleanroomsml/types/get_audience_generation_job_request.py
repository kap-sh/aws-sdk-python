"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetAudienceGenerationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_generation_job_arn


class GetAudienceGenerationJobRequest(TypedDict):
    audience_generation_job_arn: "aws_sdk_cleanroomsml.types.audience_generation_job_arn.AudienceGenerationJobArn"
    """<p>The Amazon Resource Name (ARN) of the audience generation job that you are interested in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAudienceGenerationJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAudienceGenerationJobRequest:
    out: GetAudienceGenerationJobRequest = {}  # type: ignore[typeddict-item]
    return out
