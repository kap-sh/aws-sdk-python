"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateConfiguredTableAssociationInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.configured_table_association_identifier
    import aws_sdk_cleanrooms.types.membership_identifier
    import aws_sdk_cleanrooms.types.role_arn
    import aws_sdk_cleanrooms.types.table_description


class UpdateConfiguredTableAssociationInput(TypedDict):
    configured_table_association_identifier: "aws_sdk_cleanrooms.types.configured_table_association_identifier.ConfiguredTableAssociationIdentifier"
    """<p>The unique identifier for the configured table association to update. Currently accepts the configured table association ID.</p>"""
    membership_identifier: (
        "aws_sdk_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique ID for the membership that the configured table association belongs to.</p>"""
    description: NotRequired[
        "aws_sdk_cleanrooms.types.table_description.TableDescription"
    ]
    """<p>A new description for the configured table association.</p>"""
    role_arn: NotRequired["aws_sdk_cleanrooms.types.role_arn.RoleArn"]
    """<p>The service will assume this role to access catalog metadata and query the table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfiguredTableAssociationInput) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> UpdateConfiguredTableAssociationInput:
    out: UpdateConfiguredTableAssociationInput = {}  # type: ignore[typeddict-item]
    if "description" in data:
        out["description"] = data["description"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    return out
