"""Generated from Smithy shape ``com.amazonaws.quicksight#SnapshotJobResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.anonymous_user_snapshot_job_result_list
    import aws_sdk_quicksight.types.registered_user_snapshot_job_result_list


class SnapshotJobResult(TypedDict, closed=True):
    anonymous_users: NotRequired[
        "aws_sdk_quicksight.types.anonymous_user_snapshot_job_result_list.AnonymousUserSnapshotJobResultList"
    ]
    """<p> A list of <code>AnonymousUserSnapshotJobResult</code> objects that contain information on anonymous users and their user configurations. This data provided by you when you make a <code>StartDashboardSnapshotJob</code> API call.</p>"""
    registered_users: NotRequired[
        "aws_sdk_quicksight.types.registered_user_snapshot_job_result_list.RegisteredUserSnapshotJobResultList"
    ]
    """<p>A list of <code>RegisteredUserSnapshotJobResult</code> objects that contain information about files that are requested for registered user during a <code>StartDashboardSnapshotJob</code> API call.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotJobResult) -> dict:
    out: dict = {}
    if "anonymous_users" in value:
        import aws_sdk_quicksight.types.anonymous_user_snapshot_job_result_list

        out["AnonymousUsers"] = (
            aws_sdk_quicksight.types.anonymous_user_snapshot_job_result_list.serialize_json(
                value["anonymous_users"]
            )
        )
    if "registered_users" in value:
        import aws_sdk_quicksight.types.registered_user_snapshot_job_result_list

        out["RegisteredUsers"] = (
            aws_sdk_quicksight.types.registered_user_snapshot_job_result_list.serialize_json(
                value["registered_users"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapshotJobResult:
    out: SnapshotJobResult = {}  # type: ignore[typeddict-item]
    if "AnonymousUsers" in data:
        import aws_sdk_quicksight.types.anonymous_user_snapshot_job_result_list

        out["anonymous_users"] = (
            aws_sdk_quicksight.types.anonymous_user_snapshot_job_result_list.deserialize_json(
                data["AnonymousUsers"]
            )
        )
    if "RegisteredUsers" in data:
        import aws_sdk_quicksight.types.registered_user_snapshot_job_result_list

        out["registered_users"] = (
            aws_sdk_quicksight.types.registered_user_snapshot_job_result_list.deserialize_json(
                data["RegisteredUsers"]
            )
        )
    return out
