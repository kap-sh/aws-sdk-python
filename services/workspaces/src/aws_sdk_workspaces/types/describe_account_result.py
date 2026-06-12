"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeAccountResult``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.dedicated_tenancy_account_type
    import aws_sdk_workspaces.types.dedicated_tenancy_management_cidr_range
    import aws_sdk_workspaces.types.dedicated_tenancy_support_result_enum
    import aws_sdk_workspaces.types.message


class DescribeAccountResult(TypedDict):
    dedicated_tenancy_support: NotRequired[
        "aws_sdk_workspaces.types.dedicated_tenancy_support_result_enum.DedicatedTenancySupportResultEnum"
    ]
    """<p>The status of BYOL (whether BYOL is enabled or disabled).</p>"""
    dedicated_tenancy_management_cidr_range: NotRequired[
        "aws_sdk_workspaces.types.dedicated_tenancy_management_cidr_range.DedicatedTenancyManagementCidrRange"
    ]
    """<p>The IP address range, specified as an IPv4 CIDR block, used for the management network interface.</p> <p>The management network interface is connected to a secure Amazon WorkSpaces management network. It is used for interactive streaming of the WorkSpace desktop to Amazon WorkSpaces clients, and to allow Amazon WorkSpaces to manage the WorkSpace.</p>"""
    dedicated_tenancy_account_type: NotRequired[
        "aws_sdk_workspaces.types.dedicated_tenancy_account_type.DedicatedTenancyAccountType"
    ]
    """<p>The type of linked account.</p>"""
    message: NotRequired["aws_sdk_workspaces.types.message.Message"]
    """<p>The text message to describe the status of BYOL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAccountResult) -> dict:
    out: dict = {}
    if "dedicated_tenancy_support" in value:
        import aws_sdk_workspaces.types.dedicated_tenancy_support_result_enum

        out["DedicatedTenancySupport"] = (
            aws_sdk_workspaces.types.dedicated_tenancy_support_result_enum.serialize_aws_json_1_1(
                value["dedicated_tenancy_support"]
            )
        )
    if "dedicated_tenancy_management_cidr_range" in value:
        out["DedicatedTenancyManagementCidrRange"] = value[
            "dedicated_tenancy_management_cidr_range"
        ]
    if "dedicated_tenancy_account_type" in value:
        import aws_sdk_workspaces.types.dedicated_tenancy_account_type

        out["DedicatedTenancyAccountType"] = (
            aws_sdk_workspaces.types.dedicated_tenancy_account_type.serialize_aws_json_1_1(
                value["dedicated_tenancy_account_type"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAccountResult:
    out: DescribeAccountResult = {}  # type: ignore[typeddict-item]
    if "DedicatedTenancySupport" in data:
        import aws_sdk_workspaces.types.dedicated_tenancy_support_result_enum

        out["dedicated_tenancy_support"] = (
            aws_sdk_workspaces.types.dedicated_tenancy_support_result_enum.deserialize_aws_json_1_1(
                data["DedicatedTenancySupport"]
            )
        )
    if "DedicatedTenancyManagementCidrRange" in data:
        out["dedicated_tenancy_management_cidr_range"] = data[
            "DedicatedTenancyManagementCidrRange"
        ]
    if "DedicatedTenancyAccountType" in data:
        import aws_sdk_workspaces.types.dedicated_tenancy_account_type

        out["dedicated_tenancy_account_type"] = (
            aws_sdk_workspaces.types.dedicated_tenancy_account_type.deserialize_aws_json_1_1(
                data["DedicatedTenancyAccountType"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    return out
