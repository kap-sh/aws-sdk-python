"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControlAssociationIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.standards_control_association_id

StandardsControlAssociationIds: TypeAlias = list[
    "aws_sdk_securityhub.types.standards_control_association_id.StandardsControlAssociationId"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControlAssociationIds) -> list:
    import aws_sdk_securityhub.types.standards_control_association_id

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.standards_control_association_id.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StandardsControlAssociationIds:
    import aws_sdk_securityhub.types.standards_control_association_id

    out: StandardsControlAssociationIds = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.standards_control_association_id.deserialize_json(
                item
            )
        )
    return out
