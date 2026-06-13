"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DeleteConfiguredAudienceModelPolicyRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.configured_audience_model_arn


class DeleteConfiguredAudienceModelPolicyRequest(TypedDict):
    configured_audience_model_arn: "aws_sdk_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model policy that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfiguredAudienceModelPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfiguredAudienceModelPolicyRequest:
    out: DeleteConfiguredAudienceModelPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
