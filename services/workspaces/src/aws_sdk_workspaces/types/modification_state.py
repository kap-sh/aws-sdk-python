"""Generated from Smithy shape ``com.amazonaws.workspaces#ModificationState``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.modification_resource_enum
    import aws_sdk_workspaces.types.modification_state_enum


class ModificationState(TypedDict):
    resource: NotRequired[
        "aws_sdk_workspaces.types.modification_resource_enum.ModificationResourceEnum"
    ]
    """<p>The resource.</p>"""
    state: NotRequired[
        "aws_sdk_workspaces.types.modification_state_enum.ModificationStateEnum"
    ]
    """<p>The modification state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModificationState) -> dict:
    out: dict = {}
    if "resource" in value:
        import aws_sdk_workspaces.types.modification_resource_enum

        out["Resource"] = (
            aws_sdk_workspaces.types.modification_resource_enum.serialize_aws_json_1_1(
                value["resource"]
            )
        )
    if "state" in value:
        import aws_sdk_workspaces.types.modification_state_enum

        out["State"] = (
            aws_sdk_workspaces.types.modification_state_enum.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModificationState:
    out: ModificationState = {}  # type: ignore[typeddict-item]
    if "Resource" in data:
        import aws_sdk_workspaces.types.modification_resource_enum

        out["resource"] = (
            aws_sdk_workspaces.types.modification_resource_enum.deserialize_aws_json_1_1(
                data["Resource"]
            )
        )
    if "State" in data:
        import aws_sdk_workspaces.types.modification_state_enum

        out["state"] = (
            aws_sdk_workspaces.types.modification_state_enum.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    return out
