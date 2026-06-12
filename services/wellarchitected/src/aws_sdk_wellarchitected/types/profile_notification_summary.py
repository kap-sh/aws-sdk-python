"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileNotificationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_wellarchitected.types.profile_arn
    import aws_sdk_wellarchitected.types.profile_name
    import aws_sdk_wellarchitected.types.profile_notification_type
    import aws_sdk_wellarchitected.types.profile_version
    import aws_sdk_wellarchitected.types.workload_id
    import aws_sdk_wellarchitected.types.workload_name


class ProfileNotificationSummary(TypedDict):
    current_profile_version: NotRequired[
        "aws_sdk_wellarchitected.types.profile_version.ProfileVersion"
    ]
    """<p>The current profile version.</p>"""
    latest_profile_version: NotRequired[
        "aws_sdk_wellarchitected.types.profile_version.ProfileVersion"
    ]
    """<p>The latest profile version.</p>"""
    type: NotRequired[
        "aws_sdk_wellarchitected.types.profile_notification_type.ProfileNotificationType"
    ]
    """<p>Type of notification.</p>"""
    profile_arn: NotRequired["aws_sdk_wellarchitected.types.profile_arn.ProfileArn"]
    """<p>The profile ARN.</p>"""
    profile_name: NotRequired["aws_sdk_wellarchitected.types.profile_name.ProfileName"]
    """<p>The profile name.</p>"""
    workload_id: NotRequired["aws_sdk_wellarchitected.types.workload_id.WorkloadId"]
    workload_name: NotRequired[
        "aws_sdk_wellarchitected.types.workload_name.WorkloadName"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileNotificationSummary) -> dict:
    out: dict = {}
    if "current_profile_version" in value:
        out["CurrentProfileVersion"] = value["current_profile_version"]
    if "latest_profile_version" in value:
        out["LatestProfileVersion"] = value["latest_profile_version"]
    if "type" in value:
        import aws_sdk_wellarchitected.types.profile_notification_type

        out["Type"] = (
            aws_sdk_wellarchitected.types.profile_notification_type.serialize_json(
                value["type"]
            )
        )
    if "profile_arn" in value:
        out["ProfileArn"] = value["profile_arn"]
    if "profile_name" in value:
        out["ProfileName"] = value["profile_name"]
    if "workload_id" in value:
        out["WorkloadId"] = value["workload_id"]
    if "workload_name" in value:
        out["WorkloadName"] = value["workload_name"]
    return out


def deserialize_json(data: dict) -> ProfileNotificationSummary:
    out: ProfileNotificationSummary = {}  # type: ignore[typeddict-item]
    if "CurrentProfileVersion" in data:
        out["current_profile_version"] = data["CurrentProfileVersion"]
    if "LatestProfileVersion" in data:
        out["latest_profile_version"] = data["LatestProfileVersion"]
    if "Type" in data:
        import aws_sdk_wellarchitected.types.profile_notification_type

        out["type"] = (
            aws_sdk_wellarchitected.types.profile_notification_type.deserialize_json(
                data["Type"]
            )
        )
    if "ProfileArn" in data:
        out["profile_arn"] = data["ProfileArn"]
    if "ProfileName" in data:
        out["profile_name"] = data["ProfileName"]
    if "WorkloadId" in data:
        out["workload_id"] = data["WorkloadId"]
    if "WorkloadName" in data:
        out["workload_name"] = data["WorkloadName"]
    return out
