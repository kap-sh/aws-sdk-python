"""Generated from Smithy shape ``com.amazonaws.dlm#ParameterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_dlm.types.parameter

ParameterList: TypeAlias = list["aws_sdk_dlm.types.parameter.Parameter"]


# --- restJson1 ser/de ---
def serialize_json(value: ParameterList) -> list:
    return list(value)


def deserialize_json(data: list) -> ParameterList:
    return list(data)
