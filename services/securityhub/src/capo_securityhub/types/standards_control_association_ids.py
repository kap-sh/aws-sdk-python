"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControlAssociationIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.standards_control_association_id

StandardsControlAssociationIds: TypeAlias = list[
    "capo_securityhub.types.standards_control_association_id.StandardsControlAssociationId"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControlAssociationIds) -> list:
    import capo_securityhub.types.standards_control_association_id

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.standards_control_association_id.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> StandardsControlAssociationIds:
    import capo_securityhub.types.standards_control_association_id

    out: StandardsControlAssociationIds = []
    for item in data:
        out.append(
            capo_securityhub.types.standards_control_association_id.deserialize_json(
                item
            )
        )
    return out
