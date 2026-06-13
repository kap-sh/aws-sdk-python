"""Generated from Smithy shape ``com.amazonaws.inspector2#SuccessfulAssociationResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.successful_association_result

SuccessfulAssociationResultList: TypeAlias = list[
    "aws_sdk_inspector2.types.successful_association_result.SuccessfulAssociationResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: SuccessfulAssociationResultList) -> list:
    import aws_sdk_inspector2.types.successful_association_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_inspector2.types.successful_association_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> SuccessfulAssociationResultList:
    import aws_sdk_inspector2.types.successful_association_result

    out: SuccessfulAssociationResultList = []
    for item in data:
        out.append(
            aws_sdk_inspector2.types.successful_association_result.deserialize_json(
                item
            )
        )
    return out
