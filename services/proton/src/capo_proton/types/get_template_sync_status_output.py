"""Generated from Smithy shape ``com.amazonaws.proton#GetTemplateSyncStatusOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.resource_sync_attempt
    import capo_proton.types.revision


class GetTemplateSyncStatusOutput(TypedDict, closed=True):
    latest_sync: NotRequired[
        "capo_proton.types.resource_sync_attempt.ResourceSyncAttempt"
    ]
    """<p>The details of the last sync that's returned by Proton.</p>"""
    latest_successful_sync: NotRequired[
        "capo_proton.types.resource_sync_attempt.ResourceSyncAttempt"
    ]
    """<p>The details of the last successful sync that's returned by Proton.</p>"""
    desired_state: NotRequired["capo_proton.types.revision.Revision"]
    """<p>The template sync desired state that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetTemplateSyncStatusOutput) -> dict:
    out: dict = {}
    if "latest_sync" in value:
        import capo_proton.types.resource_sync_attempt

        out["latestSync"] = (
            capo_proton.types.resource_sync_attempt.serialize_aws_json_1_0(
                value["latest_sync"]
            )
        )
    if "latest_successful_sync" in value:
        import capo_proton.types.resource_sync_attempt

        out["latestSuccessfulSync"] = (
            capo_proton.types.resource_sync_attempt.serialize_aws_json_1_0(
                value["latest_successful_sync"]
            )
        )
    if "desired_state" in value:
        import capo_proton.types.revision

        out["desiredState"] = capo_proton.types.revision.serialize_aws_json_1_0(
            value["desired_state"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetTemplateSyncStatusOutput:
    out: GetTemplateSyncStatusOutput = {}  # type: ignore[typeddict-item]
    if "latestSync" in data:
        import capo_proton.types.resource_sync_attempt

        out["latest_sync"] = (
            capo_proton.types.resource_sync_attempt.deserialize_aws_json_1_0(
                data["latestSync"]
            )
        )
    if "latestSuccessfulSync" in data:
        import capo_proton.types.resource_sync_attempt

        out["latest_successful_sync"] = (
            capo_proton.types.resource_sync_attempt.deserialize_aws_json_1_0(
                data["latestSuccessfulSync"]
            )
        )
    if "desiredState" in data:
        import capo_proton.types.revision

        out["desired_state"] = capo_proton.types.revision.deserialize_aws_json_1_0(
            data["desiredState"]
        )
    return out
