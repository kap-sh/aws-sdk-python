"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetCollaborationConfiguredAudienceModelAssociationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_identifier
    import capo_cleanrooms.types.configured_audience_model_association_identifier


class GetCollaborationConfiguredAudienceModelAssociationInput(TypedDict, closed=True):
    collaboration_identifier: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>A unique identifier for the collaboration that the configured audience model association belongs to. Accepts a collaboration ID.</p>"""
    configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier"
    """<p>A unique identifier for the configured audience model association that you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: GetCollaborationConfiguredAudienceModelAssociationInput,
) -> dict:
    out: dict = {}
    return out


def deserialize_json(
    data: dict,
) -> GetCollaborationConfiguredAudienceModelAssociationInput:
    out: GetCollaborationConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
    return out
