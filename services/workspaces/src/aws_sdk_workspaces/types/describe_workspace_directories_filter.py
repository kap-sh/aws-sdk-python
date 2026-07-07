"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceDirectoriesFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.describe_workspace_directories_filter_name
    import aws_sdk_workspaces.types.describe_workspace_directories_filter_values


class DescribeWorkspaceDirectoriesFilter(TypedDict, closed=True):
    name: "aws_sdk_workspaces.types.describe_workspace_directories_filter_name.DescribeWorkspaceDirectoriesFilterName"
    """<p>The name of the WorkSpaces to filter.</p>"""
    values: "aws_sdk_workspaces.types.describe_workspace_directories_filter_values.DescribeWorkspaceDirectoriesFilterValues"
    """<p>The values for filtering WorkSpaces</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceDirectoriesFilter) -> dict:
    out: dict = {}
    import aws_sdk_workspaces.types.describe_workspace_directories_filter_name

    out["Name"] = (
        aws_sdk_workspaces.types.describe_workspace_directories_filter_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    import aws_sdk_workspaces.types.describe_workspace_directories_filter_values

    out["Values"] = (
        aws_sdk_workspaces.types.describe_workspace_directories_filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceDirectoriesFilter:
    out: DescribeWorkspaceDirectoriesFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_workspaces.types.describe_workspace_directories_filter_name

        out["name"] = (
            aws_sdk_workspaces.types.describe_workspace_directories_filter_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("DescribeWorkspaceDirectoriesFilter.name required")
    if "Values" in data:
        import aws_sdk_workspaces.types.describe_workspace_directories_filter_values

        out["values"] = (
            aws_sdk_workspaces.types.describe_workspace_directories_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("DescribeWorkspaceDirectoriesFilter.values required")
    return out
