"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DeleteIdMappingTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.uuid


class DeleteIdMappingTableInput(TypedDict, closed=True):
    id_mapping_table_identifier: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the ID mapping table that you want to delete.</p>"""
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the ID mapping table that you want to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteIdMappingTableInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteIdMappingTableInput:
    out: DeleteIdMappingTableInput = {}  # type: ignore[typeddict-item]
    return out
