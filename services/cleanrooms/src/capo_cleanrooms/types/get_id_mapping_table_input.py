"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetIdMappingTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.uuid


class GetIdMappingTableInput(TypedDict, closed=True):
    id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the ID mapping table identifier that you want to retrieve.</p>"""
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the ID mapping table that you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdMappingTableInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIdMappingTableInput:
    out: GetIdMappingTableInput = {}  # type: ignore[typeddict-item]
    return out
