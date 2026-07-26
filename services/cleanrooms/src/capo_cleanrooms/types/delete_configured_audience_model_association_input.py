"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteConfiguredAudienceModelAssociationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_audience_model_association_identifier
    import capo_cleanrooms.types.membership_identifier


class DeleteConfiguredAudienceModelAssociationInput(TypedDict, closed=True):
    configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier"
    """<p>A unique identifier of the configured audience model association that you want to delete.</p>"""
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier of the membership that contains the audience model association that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfiguredAudienceModelAssociationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfiguredAudienceModelAssociationInput:
    out: DeleteConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
    return out
