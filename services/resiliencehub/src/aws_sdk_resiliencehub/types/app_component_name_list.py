"""Generated from Smithy shape ``com.amazonaws.resiliencehub#AppComponentNameList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.string255

AppComponentNameList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.string255.String255"
]


# --- restJson1 ser/de ---
def serialize_json(value: AppComponentNameList) -> list:
    return list(value)


def deserialize_json(data: list) -> AppComponentNameList:
    return list(data)
