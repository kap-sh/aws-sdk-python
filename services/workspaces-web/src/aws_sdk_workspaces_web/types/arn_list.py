"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn

ArnList: TypeAlias = list["aws_sdk_workspaces_web.types.arn.ARN"]


# --- restJson1 ser/de ---
def serialize_json(value: ArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ArnList:
    return list(data)
