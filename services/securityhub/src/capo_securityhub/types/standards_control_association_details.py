"""Generated from Smithy shape ``com.amazonaws.securityhub#StandardsControlAssociationDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.standards_control_association_detail

StandardsControlAssociationDetails: TypeAlias = list[
    "capo_securityhub.types.standards_control_association_detail.StandardsControlAssociationDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardsControlAssociationDetails) -> list:
    import capo_securityhub.types.standards_control_association_detail

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.standards_control_association_detail.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> StandardsControlAssociationDetails:
    import capo_securityhub.types.standards_control_association_detail

    out: StandardsControlAssociationDetails = []
    for item in data:
        out.append(
            capo_securityhub.types.standards_control_association_detail.deserialize_json(
                item
            )
        )
    return out
