"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateAudienceModelResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.audience_model_arn


class CreateAudienceModelResponse(TypedDict, closed=True):
    audience_model_arn: "aws_sdk_cleanroomsml.types.audience_model_arn.AudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the audience model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAudienceModelResponse) -> dict:
    out: dict = {}
    out["audienceModelArn"] = value["audience_model_arn"]
    return out


def deserialize_json(data: dict) -> CreateAudienceModelResponse:
    out: CreateAudienceModelResponse = {}  # type: ignore[typeddict-item]
    if "audienceModelArn" in data:
        out["audience_model_arn"] = data["audienceModelArn"]
    else:
        raise DeserializationError(
            "CreateAudienceModelResponse.audience_model_arn required"
        )
    return out
