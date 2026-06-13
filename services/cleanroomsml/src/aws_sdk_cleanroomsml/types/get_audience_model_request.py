"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetAudienceModelRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_model_arn


class GetAudienceModelRequest(TypedDict):
    audience_model_arn: "aws_sdk_cleanroomsml.types.audience_model_arn.AudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the audience model that you are interested in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAudienceModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAudienceModelRequest:
    out: GetAudienceModelRequest = {}  # type: ignore[typeddict-item]
    return out
