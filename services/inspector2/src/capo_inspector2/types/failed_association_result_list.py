"""Generated from Smithy shape ``com.amazonaws.inspector2#FailedAssociationResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.failed_association_result

FailedAssociationResultList: TypeAlias = list[
    "capo_inspector2.types.failed_association_result.FailedAssociationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedAssociationResultList) -> list:
    import capo_inspector2.types.failed_association_result

    out: list = []
    for item in value:
        out.append(capo_inspector2.types.failed_association_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> FailedAssociationResultList:
    import capo_inspector2.types.failed_association_result

    out: FailedAssociationResultList = []
    for item in data:
        out.append(
            capo_inspector2.types.failed_association_result.deserialize_json(item)
        )
    return out
