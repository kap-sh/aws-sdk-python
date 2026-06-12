"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceBundlesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.bundle_list
    import aws_sdk_workspaces.types.pagination_token


class DescribeWorkspaceBundlesResult(TypedDict):
    bundles: NotRequired["aws_sdk_workspaces.types.bundle_list.BundleList"]
    """<p>Information about the bundles.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. This token is valid for one day and must be used within that time frame.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceBundlesResult) -> dict:
    out: dict = {}
    if "bundles" in value:
        import aws_sdk_workspaces.types.bundle_list

        out["Bundles"] = aws_sdk_workspaces.types.bundle_list.serialize_aws_json_1_1(
            value["bundles"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkspaceBundlesResult:
    out: DescribeWorkspaceBundlesResult = {}  # type: ignore[typeddict-item]
    if "Bundles" in data:
        import aws_sdk_workspaces.types.bundle_list

        out["bundles"] = aws_sdk_workspaces.types.bundle_list.deserialize_aws_json_1_1(
            data["Bundles"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
