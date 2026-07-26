"""Generated from Smithy shape ``com.amazonaws.qbusiness#AssociatedGroups``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_qbusiness.types.associated_group

AssociatedGroups: TypeAlias = list[
    "capo_qbusiness.types.associated_group.AssociatedGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedGroups) -> list:
    import capo_qbusiness.types.associated_group

    out: list = []
    for item in value:
        out.append(capo_qbusiness.types.associated_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedGroups:
    import capo_qbusiness.types.associated_group

    out: AssociatedGroups = []
    for item in data:
        out.append(capo_qbusiness.types.associated_group.deserialize_json(item))
    return out
