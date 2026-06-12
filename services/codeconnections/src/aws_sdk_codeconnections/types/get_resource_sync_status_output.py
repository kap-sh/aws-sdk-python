"""Generated from Smithy shape ``com.amazonaws.codeconnections#GetResourceSyncStatusOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.resource_sync_attempt
    import aws_sdk_codeconnections.types.revision


class GetResourceSyncStatusOutput(TypedDict):
    desired_state: NotRequired["aws_sdk_codeconnections.types.revision.Revision"]
    """<p>The desired state of the Amazon Web Services resource for the sync status with the Git repository.</p>"""
    latest_successful_sync: NotRequired[
        "aws_sdk_codeconnections.types.resource_sync_attempt.ResourceSyncAttempt"
    ]
    """<p>The latest successful sync for the sync status with the Git repository.</p>"""
    latest_sync: (
        "aws_sdk_codeconnections.types.resource_sync_attempt.ResourceSyncAttempt"
    )
    """<p>The latest sync for the sync status with the Git repository, whether successful or not.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourceSyncStatusOutput) -> dict:
    out: dict = {}
    if "desired_state" in value:
        import aws_sdk_codeconnections.types.revision

        out["DesiredState"] = (
            aws_sdk_codeconnections.types.revision.serialize_aws_json_1_0(
                value["desired_state"]
            )
        )
    if "latest_successful_sync" in value:
        import aws_sdk_codeconnections.types.resource_sync_attempt

        out["LatestSuccessfulSync"] = (
            aws_sdk_codeconnections.types.resource_sync_attempt.serialize_aws_json_1_0(
                value["latest_successful_sync"]
            )
        )
    import aws_sdk_codeconnections.types.resource_sync_attempt

    out["LatestSync"] = (
        aws_sdk_codeconnections.types.resource_sync_attempt.serialize_aws_json_1_0(
            value["latest_sync"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourceSyncStatusOutput:
    out: GetResourceSyncStatusOutput = {}  # type: ignore[typeddict-item]
    if "DesiredState" in data:
        import aws_sdk_codeconnections.types.revision

        out["desired_state"] = (
            aws_sdk_codeconnections.types.revision.deserialize_aws_json_1_0(
                data["DesiredState"]
            )
        )
    if "LatestSuccessfulSync" in data:
        import aws_sdk_codeconnections.types.resource_sync_attempt

        out["latest_successful_sync"] = (
            aws_sdk_codeconnections.types.resource_sync_attempt.deserialize_aws_json_1_0(
                data["LatestSuccessfulSync"]
            )
        )
    if "LatestSync" in data:
        import aws_sdk_codeconnections.types.resource_sync_attempt

        out["latest_sync"] = (
            aws_sdk_codeconnections.types.resource_sync_attempt.deserialize_aws_json_1_0(
                data["LatestSync"]
            )
        )
    else:
        raise DeserializationError("GetResourceSyncStatusOutput.latest_sync required")
    return out
