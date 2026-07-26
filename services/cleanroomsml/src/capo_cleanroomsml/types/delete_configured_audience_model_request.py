"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#DeleteConfiguredAudienceModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_audience_model_arn


class DeleteConfiguredAudienceModelRequest(TypedDict, closed=True):
    configured_audience_model_arn: "capo_cleanroomsml.types.configured_audience_model_arn.ConfiguredAudienceModelArn"
    """<p>The Amazon Resource Name (ARN) of the configured audience model that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfiguredAudienceModelRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfiguredAudienceModelRequest:
    out: DeleteConfiguredAudienceModelRequest = {}  # type: ignore[typeddict-item]
    return out
