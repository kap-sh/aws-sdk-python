"""Generated from Smithy shape ``com.amazonaws.securityhub#UnprocessedStandardsControlAssociationUpdates``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.unprocessed_standards_control_association_update

UnprocessedStandardsControlAssociationUpdates: TypeAlias = list[
    "capo_securityhub.types.unprocessed_standards_control_association_update.UnprocessedStandardsControlAssociationUpdate"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedStandardsControlAssociationUpdates) -> list:
    import capo_securityhub.types.unprocessed_standards_control_association_update

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.unprocessed_standards_control_association_update.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UnprocessedStandardsControlAssociationUpdates:
    import capo_securityhub.types.unprocessed_standards_control_association_update

    out: UnprocessedStandardsControlAssociationUpdates = []
    for item in data:
        out.append(
            capo_securityhub.types.unprocessed_standards_control_association_update.deserialize_json(
                item
            )
        )
    return out
