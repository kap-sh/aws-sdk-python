"""Generated from Smithy shape ``com.amazonaws.ssm#DescribeMaintenanceWindowsResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ssm.types.maintenance_window_identity_list
    import aws_sdk_ssm.types.next_token


class DescribeMaintenanceWindowsResult(TypedDict):
    window_identities: NotRequired[
        "aws_sdk_ssm.types.maintenance_window_identity_list.MaintenanceWindowIdentityList"
    ]
    """<p>Information about the maintenance windows.</p>"""
    next_token: NotRequired["aws_sdk_ssm.types.next_token.NextToken"]
    """<p>The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMaintenanceWindowsResult) -> dict:
    out: dict = {}
    if "window_identities" in value:
        import aws_sdk_ssm.types.maintenance_window_identity_list

        out["WindowIdentities"] = (
            aws_sdk_ssm.types.maintenance_window_identity_list.serialize_aws_json_1_1(
                value["window_identities"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMaintenanceWindowsResult:
    out: DescribeMaintenanceWindowsResult = {}  # type: ignore[typeddict-item]
    if "WindowIdentities" in data:
        import aws_sdk_ssm.types.maintenance_window_identity_list

        out["window_identities"] = (
            aws_sdk_ssm.types.maintenance_window_identity_list.deserialize_aws_json_1_1(
                data["WindowIdentities"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
