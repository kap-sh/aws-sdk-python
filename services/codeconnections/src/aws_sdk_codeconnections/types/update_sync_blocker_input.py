"""Generated from Smithy shape ``com.amazonaws.codeconnections#UpdateSyncBlockerInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeconnections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeconnections.types.id
    import aws_sdk_codeconnections.types.resolved_reason
    import aws_sdk_codeconnections.types.resource_name
    import aws_sdk_codeconnections.types.sync_configuration_type


class UpdateSyncBlockerInput(TypedDict):
    id: "aws_sdk_codeconnections.types.id.Id"
    """<p>The ID of the sync blocker to be updated.</p>"""
    sync_type: (
        "aws_sdk_codeconnections.types.sync_configuration_type.SyncConfigurationType"
    )
    """<p>The sync type of the sync blocker to be updated.</p>"""
    resource_name: "aws_sdk_codeconnections.types.resource_name.ResourceName"
    """<p>The name of the resource for the sync blocker to be updated.</p>"""
    resolved_reason: "aws_sdk_codeconnections.types.resolved_reason.ResolvedReason"
    """<p>The reason for resolving the sync blocker.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateSyncBlockerInput) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import aws_sdk_codeconnections.types.sync_configuration_type

    out["SyncType"] = (
        aws_sdk_codeconnections.types.sync_configuration_type.serialize_aws_json_1_0(
            value["sync_type"]
        )
    )
    out["ResourceName"] = value["resource_name"]
    out["ResolvedReason"] = value["resolved_reason"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateSyncBlockerInput:
    out: UpdateSyncBlockerInput = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("UpdateSyncBlockerInput.id required")
    if "SyncType" in data:
        import aws_sdk_codeconnections.types.sync_configuration_type

        out["sync_type"] = (
            aws_sdk_codeconnections.types.sync_configuration_type.deserialize_aws_json_1_0(
                data["SyncType"]
            )
        )
    else:
        raise DeserializationError("UpdateSyncBlockerInput.sync_type required")
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    else:
        raise DeserializationError("UpdateSyncBlockerInput.resource_name required")
    if "ResolvedReason" in data:
        out["resolved_reason"] = data["ResolvedReason"]
    else:
        raise DeserializationError("UpdateSyncBlockerInput.resolved_reason required")
    return out
