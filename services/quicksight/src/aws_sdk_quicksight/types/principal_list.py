"""Generated from Smithy shape ``com.amazonaws.quicksight#PrincipalList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.string

PrincipalList: TypeAlias = list["aws_sdk_quicksight.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: PrincipalList) -> list:
    return list(value)


def deserialize_json(data: list) -> PrincipalList:
    return list(data)
