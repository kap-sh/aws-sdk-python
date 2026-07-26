"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteConfiguredTableAssociationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.configured_table_association_identifier
    import capo_cleanrooms.types.membership_identifier


class DeleteConfiguredTableAssociationInput(TypedDict, closed=True):
    configured_table_association_identifier: "capo_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier"
    """<p>The unique ID for the configured table association to be deleted. Currently accepts the configured table ID.</p>"""
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteConfiguredTableAssociationInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteConfiguredTableAssociationInput:
    out: DeleteConfiguredTableAssociationInput = {}  # type: ignore[typeddict-item]
    return out
