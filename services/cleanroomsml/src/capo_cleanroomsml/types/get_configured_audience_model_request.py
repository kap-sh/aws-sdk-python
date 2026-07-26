"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetConfiguredAudienceModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_audience_model_arn


class GetConfiguredAudienceModelRequest(TypedDict, closed=True):
    configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model that you are interested in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfiguredAudienceModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfiguredAudienceModelRequest:
    out: GetConfiguredAudienceModelRequest = {}  # type: ignore[typeddict-item]
    return out
