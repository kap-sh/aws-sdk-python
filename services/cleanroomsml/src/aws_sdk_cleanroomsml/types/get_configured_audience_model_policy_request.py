"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetConfiguredAudienceModelPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.configured_audience_model_arn


class GetConfiguredAudienceModelPolicyRequest(TypedDict):
    configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model that you are interested in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfiguredAudienceModelPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfiguredAudienceModelPolicyRequest:
    out: GetConfiguredAudienceModelPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
