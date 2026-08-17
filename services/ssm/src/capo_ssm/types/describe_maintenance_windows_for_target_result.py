"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowsForTargetResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.maintenance_windows_for_target_list
    import capo_ssm.types.next_token


class DescribeMaintenanceWindowsForTargetResult(TypedDict, closed=True):
    window_identities: NotRequired[
        "capo_ssm.types.maintenance_windows_for_target_list.MaintenanceWindowsForTargetList"
    ]
    """<p>Information about the maintenance window targets and tasks a managed node is associated with.</p>"""
    next_token: NotRequired["capo_ssm.types.next_token.NextToken"]
    """<p>The token for the next set of items to return. (You use this token in the next call.)</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMaintenanceWindowsForTargetResult) -> dict:
    out: dict = {}
    if "window_identities" in value:
        import capo_ssm.types.maintenance_windows_for_target_list

        out["WindowIdentities"] = (
            capo_ssm.types.maintenance_windows_for_target_list.serialize_aws_json_1_1(
                value["window_identities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMaintenanceWindowsForTargetResult:
    out: DescribeMaintenanceWindowsForTargetResult = {}  # type: ignore[typeddict-item]
    if data.get("WindowIdentities") is not None:
        import capo_ssm.types.maintenance_windows_for_target_list

        out["window_identities"] = (
            capo_ssm.types.maintenance_windows_for_target_list.deserialize_aws_json_1_1(
                data["WindowIdentities"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
