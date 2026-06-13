"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DeleteAudienceModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_model_arn


class DeleteAudienceModelRequest(TypedDict):
    audience_model_arn: "aws_sdk_cleanroomsml.types.audience_model_arn.AudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the audience model that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteAudienceModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteAudienceModelRequest:
    out: DeleteAudienceModelRequest = {}  # type: ignore[typeddict-item]
    return out
