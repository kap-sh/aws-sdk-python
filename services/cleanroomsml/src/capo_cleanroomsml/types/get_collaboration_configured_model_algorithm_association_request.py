"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetCollaborationConfiguredModelAlgorithmAssociationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn
    import capo_cleanroomsml.types.uuid


class GetCollaborationConfiguredModelAlgorithmAssociationRequest(
    TypedDict, closed=True
):
    configured_model_algorithm_association_arn: "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association that you want to return information about.</p>"""
    collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID for the collaboration that contains the configured model algorithm association that you want to return information about.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: GetCollaborationConfiguredModelAlgorithmAssociationRequest,
) -> dict:
    out: dict = {}
    return out


def deserialize_json(
    data: dict,
) -> GetCollaborationConfiguredModelAlgorithmAssociationRequest:
    out: GetCollaborationConfiguredModelAlgorithmAssociationRequest = {}  # type: ignore[typeddict-item]
    return out
