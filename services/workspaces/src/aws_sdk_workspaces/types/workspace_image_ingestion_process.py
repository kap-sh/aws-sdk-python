"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceImageIngestionProcess``."""

from typing import Literal, TypeAlias, cast

WorkspaceImageIngestionProcess: TypeAlias = Literal[
    "BYOL_REGULAR",
    "BYOL_GRAPHICS",
    "BYOL_GRAPHICSPRO",
    "BYOL_GRAPHICS_G4DN",
    "BYOL_REGULAR_WSP",
    "BYOL_GRAPHICS_G4DN_WSP",
    "BYOL_REGULAR_BYOP",
    "BYOL_GRAPHICS_G4DN_BYOP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WorkspaceImageIngestionProcess) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceImageIngestionProcess:
    return cast(WorkspaceImageIngestionProcess, data)
