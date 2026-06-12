"""Generated from Smithy shape ``com.amazonaws.workspaces#ListAvailableManagementCidrRangesResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.dedicated_tenancy_cidr_range_list
    import aws_sdk_workspaces.types.pagination_token


class ListAvailableManagementCidrRangesResult(TypedDict):
    management_cidr_ranges: NotRequired[
        "aws_sdk_workspaces.types.dedicated_tenancy_cidr_range_list.DedicatedTenancyCidrRangeList"
    ]
    """<p>The list of available IP address ranges, specified as IPv4 CIDR blocks.</p>"""
    next_token: NotRequired["aws_sdk_workspaces.types.pagination_token.PaginationToken"]
    """<p>The token to use to retrieve the next page of results. This value is null when there are no more results to return. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAvailableManagementCidrRangesResult) -> dict:
    out: dict = {}
    if "management_cidr_ranges" in value:
        import aws_sdk_workspaces.types.dedicated_tenancy_cidr_range_list

        out["ManagementCidrRanges"] = (
            aws_sdk_workspaces.types.dedicated_tenancy_cidr_range_list.serialize_aws_json_1_1(
                value["management_cidr_ranges"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAvailableManagementCidrRangesResult:
    out: ListAvailableManagementCidrRangesResult = {}  # type: ignore[typeddict-item]
    if "ManagementCidrRanges" in data:
        import aws_sdk_workspaces.types.dedicated_tenancy_cidr_range_list

        out["management_cidr_ranges"] = (
            aws_sdk_workspaces.types.dedicated_tenancy_cidr_range_list.deserialize_aws_json_1_1(
                data["ManagementCidrRanges"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
