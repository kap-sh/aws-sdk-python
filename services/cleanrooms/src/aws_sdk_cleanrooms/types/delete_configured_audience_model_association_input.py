"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteConfiguredAudienceModelAssociationInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_audience_model_association_identifier
    import aws_sdk_cleanrooms.types.membership_identifier


class DeleteConfiguredAudienceModelAssociationInput(TypedDict):
    configured_audience_model_association_identifier: "aws_sdk_cleanrooms.types.configured_audience_model_association_identifier.ConfiguredAudienceModelAssociationIdentifier"
    """<p>A unique identifier of the configured audience model association that you want to delete.</p>"""
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier of the membership that contains the audience model association that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfiguredAudienceModelAssociationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfiguredAudienceModelAssociationInput:
    out: DeleteConfiguredAudienceModelAssociationInput = {}  # type: ignore[typeddict-item]
    return out
