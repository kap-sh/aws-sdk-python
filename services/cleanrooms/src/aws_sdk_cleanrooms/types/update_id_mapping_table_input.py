"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateIdMappingTableInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.kms_key_arn
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.resource_description
    import aws_sdk_cleanrooms.types.uuid


class UpdateIdMappingTableInput(TypedDict):
    id_mapping_table_identifier: "aws_sdk_cleanrooms.types.uuid.UUID"
    """<p>The unique identifier of the ID mapping table that you want to update.</p>"""
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the ID mapping table that you want to update.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>A new description for the ID mapping table.</p>"""
    kms_key_arn: NotRequired["aws_sdk_cleanrooms.types.kms_key_arn.KMSKeyArn"]
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
