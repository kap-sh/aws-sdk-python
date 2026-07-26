"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateIdMappingTableInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.kms_key_arn
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.uuid


class UpdateIdMappingTableInput(TypedDict, closed=True):
    id_mapping_table_identifier: "capo_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the ID mapping table that you want to update.</p>"""
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the ID mapping table that you want to update.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>A new description for the ID mapping table.</p>"""
    kms_key_arn: NotRequired["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services KMS key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIdMappingTableInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> UpdateIdMappingTableInput:
    out: UpdateIdMappingTableInput = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
