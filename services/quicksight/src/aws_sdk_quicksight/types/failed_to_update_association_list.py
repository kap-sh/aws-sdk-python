"""Generated from Smithy shape ``com.amazonaws.quicksight#FailedToUpdateAssociationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.failed_to_update_association

FailedToUpdateAssociationList: TypeAlias = list[
    "aws_sdk_quicksight.types.failed_to_update_association.FailedToUpdateAssociation"
]


# --- restJson1 ser/de ---
def serialize_json(value: FailedToUpdateAssociationList) -> list:
    import aws_sdk_quicksight.types.failed_to_update_association

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.failed_to_update_association.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> FailedToUpdateAssociationList:
    import aws_sdk_quicksight.types.failed_to_update_association

    out: FailedToUpdateAssociationList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.failed_to_update_association.deserialize_json(item)
        )
    return out
