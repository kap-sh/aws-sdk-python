"""Generated from Smithy shape ``com.amazonaws.cleanrooms#GetIdMappingTableInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.uuid


class GetIdMappingTableInput(TypedDict):
    id_mapping_table_identifier: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the ID mapping table identifier that you want to retrieve.</p>"""
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the ID mapping table that you want to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetIdMappingTableInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetIdMappingTableInput:
    out: GetIdMappingTableInput = {}  # type: ignore[typeddict-item]
    return out
