"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ProfileNotificationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_wellarchitected.types.profile_arn
    import capo_wellarchitected.types.profile_name
    import capo_wellarchitected.types.profile_notification_type
    import capo_wellarchitected.types.profile_version
    import capo_wellarchitected.types.workload_id
    import capo_wellarchitected.types.workload_name


class ProfileNotificationSummary(TypedDict, closed=True):
    current_profile_version: NotRequired[
        "capo_wellarchitected.types.profile_version.ProfileVersion"
    ]
    """<p>The current profile version.</p>"""
    latest_profile_version: NotRequired[
        "capo_wellarchitected.types.profile_version.ProfileVersion"
    ]
    """<p>The latest profile version.</p>"""
    type: NotRequired[
        "capo_wellarchitected.types.profile_notification_type.ProfileNotificationType"
    ]
    """<p>Type of notification.</p>"""
    profile_arn: NotRequired["capo_wellarchitected.types.profile_arn.ProfileArn"]
    """<p>The profile ARN.</p>"""
    profile_name: NotRequired["capo_wellarchitected.types.profile_name.ProfileName"]
    """<p>The profile name.</p>"""
    workload_id: NotRequired["capo_wellarchitected.types.workload_id.WorkloadId"]
    workload_name: NotRequired["capo_wellarchitected.types.workload_name.WorkloadName"]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileNotificationSummary) -> dict:
    out: dict = {}
    if "current_profile_version" in value:
        out["CurrentProfileVersion"] = value["current_profile_version"]
    if "latest_profile_version" in value:
        out["LatestProfileVersion"] = value["latest_profile_version"]
    if "type" in value:
        import capo_wellarchitected.types.profile_notification_type

        out["Type"] = (
            capo_wellarchitected.types.profile_notification_type.serialize_json(
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
        import capo_wellarchitected.types.profile_notification_type

        out["type"] = (
            capo_wellarchitected.types.profile_notification_type.deserialize_json(
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
