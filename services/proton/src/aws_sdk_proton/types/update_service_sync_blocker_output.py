"""Generated from Smithy shape ``com.amazonaws.proton#UpdateServiceSyncBlockerOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.resource_name
    import aws_sdk_proton.types.sync_blocker


class UpdateServiceSyncBlockerOutput(TypedDict, closed=True):
    service_name: "aws_sdk_proton.types.resource_name.ResourceName"
    """<p>The name of the service that you want to update the service sync blocker for.</p>"""
    service_instance_name: NotRequired[
        "aws_sdk_proton.types.resource_name.ResourceName"
    ]
    """<p>The name of the service instance that you want to update the service sync blocker for.</p>"""
    service_sync_blocker: "aws_sdk_proton.types.sync_blocker.SyncBlocker"
    """<p>The detailed data on the service sync blocker that was updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateServiceSyncBlockerOutput) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    import aws_sdk_proton.types.sync_blocker

    out["serviceSyncBlocker"] = (
        aws_sdk_proton.types.sync_blocker.serialize_aws_json_1_0(
            value["service_sync_blocker"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateServiceSyncBlockerOutput:
    out: UpdateServiceSyncBlockerOutput = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError(
            "UpdateServiceSyncBlockerOutput.service_name required"
        )
    if "serviceInstanceName" in data:
        out["service_instance_name"] = data["serviceInstanceName"]
    if "serviceSyncBlocker" in data:
        import aws_sdk_proton.types.sync_blocker

        out["service_sync_blocker"] = (
            aws_sdk_proton.types.sync_blocker.deserialize_aws_json_1_0(
                data["serviceSyncBlocker"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateServiceSyncBlockerOutput.service_sync_blocker required"
        )
    return out
