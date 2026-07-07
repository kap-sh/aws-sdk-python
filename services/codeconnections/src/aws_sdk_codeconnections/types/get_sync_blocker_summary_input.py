"""Generated from Smithy shape ``com.amazonaws.codeconnections#GetSyncBlockerSummaryInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.resource_name
    import aws_sdk_codeconnections.types.sync_configuration_type


class GetSyncBlockerSummaryInput(TypedDict, closed=True):
    sync_type: (
        "aws_sdk_codeconnections.types.sync_configuration_type.SyncConfigurationType"
    )
    """<p>The sync type for the sync blocker summary.</p>"""
    resource_name: "aws_sdk_codeconnections.types.resource_name.ResourceName"
    """<p>The name of the Amazon Web Services resource currently blocked from automatically being synced from a Git repository.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSyncBlockerSummaryInput) -> dict:
    out: dict = {}
    import aws_sdk_codeconnections.types.sync_configuration_type

    out["SyncType"] = (
        aws_sdk_codeconnections.types.sync_configuration_type.serialize_aws_json_1_0(
            value["sync_type"]
        )
    )
    out["ResourceName"] = value["resource_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSyncBlockerSummaryInput:
    out: GetSyncBlockerSummaryInput = {}  # type: ignore[typeddict-item]
    if "SyncType" in data:
        import aws_sdk_codeconnections.types.sync_configuration_type

        out["sync_type"] = (
            aws_sdk_codeconnections.types.sync_configuration_type.deserialize_aws_json_1_0(
                data["SyncType"]
            )
        )
    else:
        raise DeserializationError("GetSyncBlockerSummaryInput.sync_type required")
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    else:
        raise DeserializationError("GetSyncBlockerSummaryInput.resource_name required")
    return out
