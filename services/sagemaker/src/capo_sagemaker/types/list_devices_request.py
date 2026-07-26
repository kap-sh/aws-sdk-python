"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListDevicesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.list_max_results
    import capo_sagemaker.types.next_token
    import capo_sagemaker.types.timestamp


class ListDevicesRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_sagemaker.types.next_token.NextToken"]
    """<p>The response from the last list when returning a list large enough to need tokening.</p>"""
    max_results: NotRequired["capo_sagemaker.types.list_max_results.ListMaxResults"]
    """<p>Maximum number of results to select.</p>"""
    latest_heartbeat_after: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>Select fleets where the job was updated after X</p>"""
    model_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>A filter that searches devices that contains this name in any of their models.</p>"""
    device_fleet_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>Filter for fleets containing this name in their device fleet name.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListDevicesRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "latest_heartbeat_after" in value:
        import capo_sagemaker.types.timestamp

        out["LatestHeartbeatAfter"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["latest_heartbeat_after"]
            )
        )
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "device_fleet_name" in value:
        out["DeviceFleetName"] = value["device_fleet_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListDevicesRequest:
    out: ListDevicesRequest = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "LatestHeartbeatAfter" in data:
        import capo_sagemaker.types.timestamp

        out["latest_heartbeat_after"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LatestHeartbeatAfter"]
            )
        )
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "DeviceFleetName" in data:
        out["device_fleet_name"] = data["DeviceFleetName"]
    return out
