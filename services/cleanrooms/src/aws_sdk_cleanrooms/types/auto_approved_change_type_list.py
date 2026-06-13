"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AutoApprovedChangeTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanrooms.types.auto_approved_change_type

AutoApprovedChangeTypeList: TypeAlias = list[
    "aws_sdk_cleanrooms.types.auto_approved_change_type.AutoApprovedChangeType"
]


# --- restJson1 ser/de ---
def serialize_json(value: AutoApprovedChangeTypeList) -> list:
    import aws_sdk_cleanrooms.types.auto_approved_change_type

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanrooms.types.auto_approved_change_type.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AutoApprovedChangeTypeList:
    import aws_sdk_cleanrooms.types.auto_approved_change_type

    out: AutoApprovedChangeTypeList = []
    for item in data:
        out.append(
            aws_sdk_cleanrooms.types.auto_approved_change_type.deserialize_json(item)
        )
    return out
