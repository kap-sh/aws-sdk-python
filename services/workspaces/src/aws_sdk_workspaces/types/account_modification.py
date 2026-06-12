"""Generated from Smithy shape ``com.amazonaws.workspaces#AccountModification``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.dedicated_tenancy_management_cidr_range
    import aws_sdk_workspaces.types.dedicated_tenancy_modification_state_enum
    import aws_sdk_workspaces.types.dedicated_tenancy_support_result_enum
    import aws_sdk_workspaces.types.description
    import aws_sdk_workspaces.types.timestamp
    import aws_sdk_workspaces.types.workspace_error_code


class AccountModification(TypedDict):
    modification_state: NotRequired[
        "aws_sdk_workspaces.types.dedicated_tenancy_modification_state_enum.DedicatedTenancyModificationStateEnum"
    ]
    """<p>The state of the modification to the configuration of BYOL.</p>"""
    dedicated_tenancy_support: NotRequired[
        "aws_sdk_workspaces.types.dedicated_tenancy_support_result_enum.DedicatedTenancySupportResultEnum"
    ]
    """<p>The status of BYOL (whether BYOL is being enabled or disabled).</p>"""
    dedicated_tenancy_management_cidr_range: NotRequired[
        "aws_sdk_workspaces.types.dedicated_tenancy_management_cidr_range.DedicatedTenancyManagementCidrRange"
    ]
    """<p>The IP address range, specified as an IPv4 CIDR block, for the management network interface used for the account.</p>"""
    start_time: NotRequired["aws_sdk_workspaces.types.timestamp.Timestamp"]
    """<p>The timestamp when the modification of the BYOL configuration was started.</p>"""
    error_code: NotRequired[
        "aws_sdk_workspaces.types.workspace_error_code.WorkspaceErrorCode"
    ]
    """<p>The error code that is returned if the configuration of BYOL cannot be modified.</p>"""
    error_message: NotRequired["aws_sdk_workspaces.types.description.Description"]
    """<p>The text of the error message that is returned if the configuration of BYOL cannot be modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AccountModification) -> dict:
    out: dict = {}
    if "modification_state" in value:
        import aws_sdk_workspaces.types.dedicated_tenancy_modification_state_enum

        out["ModificationState"] = (
            aws_sdk_workspaces.types.dedicated_tenancy_modification_state_enum.serialize_aws_json_1_1(
                value["modification_state"]
            )
        )
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
    if "start_time" in value:
        import aws_sdk_workspaces.types.timestamp

        out["StartTime"] = aws_sdk_workspaces.types.timestamp.serialize_aws_json_1_1(
            value["start_time"]
        )
    if "error_code" in value:
        out["ErrorCode"] = value["error_code"]
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AccountModification:
    out: AccountModification = {}  # type: ignore[typeddict-item]
    if "ModificationState" in data:
        import aws_sdk_workspaces.types.dedicated_tenancy_modification_state_enum

        out["modification_state"] = (
            aws_sdk_workspaces.types.dedicated_tenancy_modification_state_enum.deserialize_aws_json_1_1(
                data["ModificationState"]
            )
        )
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
    if "StartTime" in data:
        import aws_sdk_workspaces.types.timestamp

        out["start_time"] = aws_sdk_workspaces.types.timestamp.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    if "ErrorCode" in data:
        out["error_code"] = data["ErrorCode"]
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    return out
