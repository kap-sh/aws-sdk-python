"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#UpdateConfiguredAudienceModelResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.configured_audience_model_arn


class UpdateConfiguredAudienceModelResponse(TypedDict):
    configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model that was updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfiguredAudienceModelResponse) -> dict:
    out: dict = {}
    out["configuredAudienceModelArn"] = value["configured_audience_model_arn"]
    return out


def deserialize_json(data: dict) -> UpdateConfiguredAudienceModelResponse:
    out: UpdateConfiguredAudienceModelResponse = {}  # type: ignore[typeddict-item]
    if "configuredAudienceModelArn" in data:
        out["configured_audience_model_arn"] = data["configuredAudienceModelArn"]
    else:
        raise DeserializationError(
            "UpdateConfiguredAudienceModelResponse.configured_audience_model_arn required"
        )
    return out
