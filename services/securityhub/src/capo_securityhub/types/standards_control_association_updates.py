"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControlAssociationUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.standards_control_association_update

StandardsControlAssociationUpdates: TypeAlias = list[
    "capo_securityhub.types.standards_control_association_update.StandardsControlAssociationUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControlAssociationUpdates) -> list:
    import capo_securityhub.types.standards_control_association_update

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.standards_control_association_update.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StandardsControlAssociationUpdates:
    import capo_securityhub.types.standards_control_association_update

    out: StandardsControlAssociationUpdates = []
    for item in data:
        out.append(
            capo_securityhub.types.standards_control_association_update.deserialize_json(
                item
            )
        )
    return out
