"""Generated from Smithy shape ``com.amazonaws.securityhub#UnprocessedStandardsControlAssociations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.unprocessed_standards_control_association

UnprocessedStandardsControlAssociations: TypeAlias = list[
    "capo_securityhub.types.unprocessed_standards_control_association.UnprocessedStandardsControlAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnprocessedStandardsControlAssociations) -> list:
    import capo_securityhub.types.unprocessed_standards_control_association

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.unprocessed_standards_control_association.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> UnprocessedStandardsControlAssociations:
    import capo_securityhub.types.unprocessed_standards_control_association

    out: UnprocessedStandardsControlAssociations = []
    for item in data:
        out.append(
            capo_securityhub.types.unprocessed_standards_control_association.deserialize_json(
                item
            )
        )
    return out
