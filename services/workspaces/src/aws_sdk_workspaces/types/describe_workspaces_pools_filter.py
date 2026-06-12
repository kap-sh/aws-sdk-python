"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolsFilter``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.describe_workspaces_pools_filter_name
    import aws_sdk_workspaces.types.describe_workspaces_pools_filter_operator
    import aws_sdk_workspaces.types.describe_workspaces_pools_filter_values


class DescribeWorkspacesPoolsFilter(TypedDict):
    name: "aws_sdk_workspaces.types.describe_workspaces_pools_filter_name.DescribeWorkspacesPoolsFilterName"
    """<p>The name of the pool to filter.</p>"""
    values: "aws_sdk_workspaces.types.describe_workspaces_pools_filter_values.DescribeWorkspacesPoolsFilterValues"
    """<p>The values for filtering WorkSpaces Pools.</p>"""
    operator: "aws_sdk_workspaces.types.describe_workspaces_pools_filter_operator.DescribeWorkspacesPoolsFilterOperator"
    """<p>The operator values for filtering WorkSpaces Pools.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesPoolsFilter) -> dict:
    out: dict = {}
    import aws_sdk_workspaces.types.describe_workspaces_pools_filter_name

    out["Name"] = (
        aws_sdk_workspaces.types.describe_workspaces_pools_filter_name.serialize_aws_json_1_1(
            value["name"]
        )
    )
    import aws_sdk_workspaces.types.describe_workspaces_pools_filter_values

    out["Values"] = (
        aws_sdk_workspaces.types.describe_workspaces_pools_filter_values.serialize_aws_json_1_1(
            value["values"]
        )
    )
    import aws_sdk_workspaces.types.describe_workspaces_pools_filter_operator

    out["Operator"] = (
        aws_sdk_workspaces.types.describe_workspaces_pools_filter_operator.serialize_aws_json_1_1(
            value["operator"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspacesPoolsFilter:
    out: DescribeWorkspacesPoolsFilter = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        import aws_sdk_workspaces.types.describe_workspaces_pools_filter_name

        out["name"] = (
            aws_sdk_workspaces.types.describe_workspaces_pools_filter_name.deserialize_aws_json_1_1(
                data["Name"]
            )
        )
    else:
        raise DeserializationError("DescribeWorkspacesPoolsFilter.name required")
    if "Values" in data:
        import aws_sdk_workspaces.types.describe_workspaces_pools_filter_values

        out["values"] = (
            aws_sdk_workspaces.types.describe_workspaces_pools_filter_values.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    else:
        raise DeserializationError("DescribeWorkspacesPoolsFilter.values required")
    if "Operator" in data:
        import aws_sdk_workspaces.types.describe_workspaces_pools_filter_operator

        out["operator"] = (
            aws_sdk_workspaces.types.describe_workspaces_pools_filter_operator.deserialize_aws_json_1_1(
                data["Operator"]
            )
        )
    else:
        raise DeserializationError("DescribeWorkspacesPoolsFilter.operator required")
    return out
