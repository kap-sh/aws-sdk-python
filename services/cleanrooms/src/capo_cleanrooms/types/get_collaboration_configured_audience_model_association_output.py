"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetCollaborationConfiguredAudienceModelAssociationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_configured_audience_model_association


class GetCollaborationConfiguredAudienceModelAssociationOutput(TypedDict, closed=True):
    collaboration_configured_audience_model_association: "capo_cleanrooms.types.collaboration_configured_audience_model_association.CollaborationConfiguredAudienceModelAssociation"
    """<p>The metadata of the configured audience model association.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: GetCollaborationConfiguredAudienceModelAssociationOutput,
) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.collaboration_configured_audience_model_association

    out["collaborationConfiguredAudienceModelAssociation"] = (
        capo_cleanrooms.types.collaboration_configured_audience_model_association.serialize_json(
            value["collaboration_configured_audience_model_association"]
        )
    )
    return out


def deserialize_json(
    data: dict,
) -> GetCollaborationConfiguredAudienceModelAssociationOutput:
    out: GetCollaborationConfiguredAudienceModelAssociationOutput = {}  # type: ignore[typeddict-item]
    if "collaborationConfiguredAudienceModelAssociation" in data:
        import capo_cleanrooms.types.collaboration_configured_audience_model_association

        out["collaboration_configured_audience_model_association"] = (
            capo_cleanrooms.types.collaboration_configured_audience_model_association.deserialize_json(
                data["collaborationConfiguredAudienceModelAssociation"]
            )
        )
    else:
        raise DeserializationError(
            "GetCollaborationConfiguredAudienceModelAssociationOutput.collaboration_configured_audience_model_association required"
        )
    return out
