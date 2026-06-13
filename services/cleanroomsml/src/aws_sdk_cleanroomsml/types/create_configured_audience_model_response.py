"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateConfiguredAudienceModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.configured_audience_model_arn


class CreateConfiguredAudienceModelResponse(TypedDict):
    configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateConfiguredAudienceModelResponse) -> dict:
    out: dict = {}
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    return out


def deserialize_json(data: dict) -> CreateConfiguredAudienceModelResponse:
    out: CreateConfiguredAudienceModelResponse = {}  # type: ignore[typeddict-item]
    if "configuredAudienceModelArn" in data:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        raise DeserializationError(
            "CreateConfiguredAudienceModelResponse.configured_audience_model_arn required"
        )
    return out
