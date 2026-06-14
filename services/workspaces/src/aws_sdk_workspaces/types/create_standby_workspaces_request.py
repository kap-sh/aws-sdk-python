"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateStandbyWorkspacesRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.region
    import aws_sdk_workspaces.types.standby_workspaces_list


class CreateStandbyWorkspacesRequest(TypedDict):
    primary_region: "aws_sdk_workspaces.types.region.Region"
    """<p>The Region of the primary WorkSpace.</p>"""
    standby_workspaces: (
        "aws_sdk_workspaces.types.standby_workspaces_list.StandbyWorkspacesList"
    )
    """<p>Information about the standby WorkSpace to be created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStandbyWorkspacesRequest) -> dict:
    out: dict = {}
    out["PrimaryRegion"] = value["primary_region"]
    import aws_sdk_workspaces.types.standby_workspaces_list

    out["StandbyWorkspaces"] = (
        aws_sdk_workspaces.types.standby_workspaces_list.serialize_aws_json_1_1(
            value["standby_workspaces"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStandbyWorkspacesRequest:
    out: CreateStandbyWorkspacesRequest = {}  # type: ignore[typeddict-item]
    if "PrimaryRegion" in data:
        out["primary_region"] = data["PrimaryRegion"]
    else:
        raise DeserializationError(
            "CreateStandbyWorkspacesRequest.primary_region required"
        )
    if "StandbyWorkspaces" in data:
        import aws_sdk_workspaces.types.standby_workspaces_list

        out["standby_workspaces"] = (
            aws_sdk_workspaces.types.standby_workspaces_list.deserialize_aws_json_1_1(
                data["StandbyWorkspaces"]
            )
        )
    else:
        raise DeserializationError(
            "CreateStandbyWorkspacesRequest.standby_workspaces required"
        )
    return out
