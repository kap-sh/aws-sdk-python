"""Generated from Smithy shape ``com.amazonaws.eks#IncludeClustersList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.string

IncludeClustersList: TypeAlias = list["aws_sdk_eks.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: IncludeClustersList) -> list:
    return list(value)


def deserialize_json(data: list) -> IncludeClustersList:
    return list(data)
