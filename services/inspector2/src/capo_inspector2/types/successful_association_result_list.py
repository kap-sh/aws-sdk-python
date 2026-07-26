"""Generated from Smithy shape ``com.amazonaws.inspector2#SuccessfulAssociationResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.successful_association_result

SuccessfulAssociationResultList: TypeAlias = list[
    "capo_inspector2.types.successful_association_result.SuccessfulAssociationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulAssociationResultList) -> list:
    import capo_inspector2.types.successful_association_result

    out: list = []
    for item in value:
        out.append(
            capo_inspector2.types.successful_association_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SuccessfulAssociationResultList:
    import capo_inspector2.types.successful_association_result

    out: SuccessfulAssociationResultList = []
    for item in data:
        out.append(
            capo_inspector2.types.successful_association_result.deserialize_json(item)
        )
    return out
