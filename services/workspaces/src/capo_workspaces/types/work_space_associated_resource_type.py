"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkSpaceAssociatedResourceType``."""

from typing import Literal, TypeAlias, cast

WorkSpaceAssociatedResourceType: TypeAlias = Literal["APPLICATION",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkSpaceAssociatedResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkSpaceAssociatedResourceType:
    return cast(WorkSpaceAssociatedResourceType, data)
