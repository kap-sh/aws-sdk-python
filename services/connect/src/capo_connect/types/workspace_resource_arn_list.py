"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceResourceArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.arn

WorkspaceResourceArnList: TypeAlias = list["capo_connect.types.arn.ARN"]


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceResourceArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> WorkspaceResourceArnList:
    return list(data)
