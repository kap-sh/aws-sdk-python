"""Generated from Smithy shape ``com.amazonaws.appflow#SupportedValueList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_appflow.types.value

SupportedValueList: TypeAlias = list["aws_sdk_appflow.types.value.Value"]


# --- restJson1 ser/de ---
def serialize_json(value: SupportedValueList) -> list:
    return list(value)


def deserialize_json(data: list) -> SupportedValueList:
    return list(data)
