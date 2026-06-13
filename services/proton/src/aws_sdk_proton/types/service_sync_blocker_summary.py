"""Generated from Smithy shape ``com.amazonaws.proton#ServiceSyncBlockerSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.latest_sync_blockers


class ServiceSyncBlockerSummary(TypedDict):
    service_name: "str"
    """<p>The name of the service that you want to get the sync blocker summary for. If given a service instance name and a service name, it will return the blockers only applying to the instance that is blocked.</p> <p>If given only a service name, it will return the blockers that apply to all of the instances. In order to get the blockers for a single instance, you will need to make two distinct calls, one to get the sync blocker summary for the service and the other to get the sync blocker for the service instance.</p>"""
    service_instance_name: NotRequired["str"]
    """<p>The name of the service instance that you want sync your service configuration with.</p>"""
    latest_blockers: NotRequired[
        "aws_sdk_proton.types.latest_sync_blockers.LatestSyncBlockers"
    ]
    """<p>The latest active blockers for the synced service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceSyncBlockerSummary) -> dict:
    out: dict = {}
    out["serviceName"] = value["service_name"]
    if "service_instance_name" in value:
        out["serviceInstanceName"] = value["service_instance_name"]
    if "latest_blockers" in value:
        import aws_sdk_proton.types.latest_sync_blockers

        out["latestBlockers"] = (
            aws_sdk_proton.types.latest_sync_blockers.serialize_aws_json_1_0(
                value["latest_blockers"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ServiceSyncBlockerSummary:
    out: ServiceSyncBlockerSummary = {}  # type: ignore[typeddict-item]
    if "serviceName" in data:
        out["service_name"] = data["serviceName"]
    else:
        raise DeserializationError("ServiceSyncBlockerSummary.service_name required")
    if "serviceInstanceName" in data:
        out["service_instance_name"] = data["serviceInstanceName"]
    if "latestBlockers" in data:
        import aws_sdk_proton.types.latest_sync_blockers

        out["latest_blockers"] = (
            aws_sdk_proton.types.latest_sync_blockers.deserialize_aws_json_1_0(
                data["latestBlockers"]
            )
        )
    return out
