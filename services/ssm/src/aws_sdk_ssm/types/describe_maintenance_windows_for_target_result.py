"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowsForTargetResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_windows_for_target_list
    import aws_sdk_ssm.types.next_token


class DescribeMaintenanceWindowsForTargetResult(TypedDict):
    window_identities: NotRequired[
        "aws_sdk_ssm.types.maintenance_windows_for_target_list.MaintenanceWindowsForTargetList"
    ]
    """<p>Information about the maintenance window targets and tasks a managed node is associated with.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You use this token in the next call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMaintenanceWindowsForTargetResult) -> dict:
    out: dict = {}
    if "window_identities" in value:
        import aws_sdk_ssm.types.maintenance_windows_for_target_list

        out["WindowIdentities"] = (
            aws_sdk_ssm.types.maintenance_windows_for_target_list.serialize_aws_json_1_1(
                value["window_identities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMaintenanceWindowsForTargetResult:
    out: DescribeMaintenanceWindowsForTargetResult = {}  # type: ignore[typeddict-item]
    if "WindowIdentities" in data:
        import aws_sdk_ssm.types.maintenance_windows_for_target_list

        out["window_identities"] = (
            aws_sdk_ssm.types.maintenance_windows_for_target_list.deserialize_aws_json_1_1(
                data["WindowIdentities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
