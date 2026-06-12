"""Generated from Smithy shape ``com.amazonaws.codecatalyst#StopDevEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.uuid


class StopDevEnvironmentRequest(TypedDict):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    id: "aws_sdk_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the Dev Environment. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopDevEnvironmentRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> StopDevEnvironmentRequest:
    out: StopDevEnvironmentRequest = {}  # type: ignore[typeddict-item]
    return out
