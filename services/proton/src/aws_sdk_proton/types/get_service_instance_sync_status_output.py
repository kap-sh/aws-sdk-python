"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceInstanceSyncStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_sync_attempt
    import aws_sdk_proton.types.revision


class GetServiceInstanceSyncStatusOutput(TypedDict, closed=True):
    latest_sync: NotRequired[
        "aws_sdk_proton.types.resource_sync_attempt.ResourceSyncAttempt"
    ]
    """<p>The detailed data of the latest sync with the service instance.</p>"""
    latest_successful_sync: NotRequired[
        "aws_sdk_proton.types.resource_sync_attempt.ResourceSyncAttempt"
    ]
    """<p>The detailed data of the latest successful sync with the service instance.</p>"""
    desired_state: NotRequired["aws_sdk_proton.types.revision.Revision"]
    """<p>The service instance sync desired state that's returned by Proton</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceInstanceSyncStatusOutput) -> dict:
    out: dict = {}
    if "latest_sync" in value:
        import aws_sdk_proton.types.resource_sync_attempt

        out["latestSync"] = (
            aws_sdk_proton.types.resource_sync_attempt.serialize_aws_json_1_0(
                value["latest_sync"]
            )
        )
    if "latest_successful_sync" in value:
        import aws_sdk_proton.types.resource_sync_attempt

        out["latestSuccessfulSync"] = (
            aws_sdk_proton.types.resource_sync_attempt.serialize_aws_json_1_0(
                value["latest_successful_sync"]
            )
        )
    if "desired_state" in value:
        import aws_sdk_proton.types.revision

        out["desiredState"] = aws_sdk_proton.types.revision.serialize_aws_json_1_0(
            value["desired_state"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceInstanceSyncStatusOutput:
    out: GetServiceInstanceSyncStatusOutput = {}  # type: ignore[typeddict-item]
    if "latestSync" in data:
        import aws_sdk_proton.types.resource_sync_attempt

        out["latest_sync"] = (
            aws_sdk_proton.types.resource_sync_attempt.deserialize_aws_json_1_0(
                data["latestSync"]
            )
        )
    if "latestSuccessfulSync" in data:
        import aws_sdk_proton.types.resource_sync_attempt

        out["latest_successful_sync"] = (
            aws_sdk_proton.types.resource_sync_attempt.deserialize_aws_json_1_0(
                data["latestSuccessfulSync"]
            )
        )
    if "desiredState" in data:
        import aws_sdk_proton.types.revision

        out["desired_state"] = aws_sdk_proton.types.revision.deserialize_aws_json_1_0(
            data["desiredState"]
        )
    return out
