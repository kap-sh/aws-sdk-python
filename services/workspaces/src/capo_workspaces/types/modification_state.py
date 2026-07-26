"""Generated from Smithy shape ``com.amazonaws.workspaces#ModificationState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.modification_resource_enum
    import capo_workspaces.types.modification_state_enum


class ModificationState(TypedDict, closed=True):
    resource: NotRequired[
        "capo_workspaces.types.modification_resource_enum.ModificationResourceEnum"
    ]
    """<p>The resource.</p>"""
    state: NotRequired[
        "capo_workspaces.types.modification_state_enum.ModificationStateEnum"
    ]
    """<p>The modification state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModificationState) -> dict:
    out: dict = {}
    if "resource" in value:
        import capo_workspaces.types.modification_resource_enum

        out["Resource"] = (
            capo_workspaces.types.modification_resource_enum.serialize_aws_json_1_1(
                value["resource"]
            )
        )
    if "state" in value:
        import capo_workspaces.types.modification_state_enum

        out["State"] = (
            capo_workspaces.types.modification_state_enum.serialize_aws_json_1_1(
                value["state"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModificationState:
    out: ModificationState = {}  # type: ignore[typeddict-item]
    if "Resource" in data:
        import capo_workspaces.types.modification_resource_enum

        out["resource"] = (
            capo_workspaces.types.modification_resource_enum.deserialize_aws_json_1_1(
                data["Resource"]
            )
        )
    if "State" in data:
        import capo_workspaces.types.modification_state_enum

        out["state"] = (
            capo_workspaces.types.modification_state_enum.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    return out
