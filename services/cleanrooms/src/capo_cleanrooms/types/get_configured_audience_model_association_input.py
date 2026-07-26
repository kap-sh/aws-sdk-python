"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetConfiguredAudienceModelAssociationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_audience_model_association_identifier
    import capo_cleanrooms.types.membership_identifier


class GetConfiguredAudienceModelAssociationInput(TypedDict, closed=True):
    configured_audience_model_association_identifier: "capo_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier"
    """<p>A unique identifier for the configured audience model association that you want to retrieve.</p>"""
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for the membership that contains the configured audience model association that you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfiguredAudienceModelAssociationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetConfiguredAudienceModelAssociationInput:
    out: GetConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
    return out
