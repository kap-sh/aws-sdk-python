"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AlarmReferenceIdList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.string500

AlarmReferenceIdList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.string500.String500"
]


# --- restJson1 ser/de ---
def serialize_json(value: AlarmReferenceIdList) -> list:
    return list(value)


def deserialize_json(data: list) -> AlarmReferenceIdList:
    return list(data)
