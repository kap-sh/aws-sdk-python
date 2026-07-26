"""Generated from Smithy shape ``com.amazonaws.machinelearning#RealtimeEndpointInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.epoch_time
    import capo_machine_learning.types.integer_type
    import capo_machine_learning.types.realtime_endpoint_status
    import capo_machine_learning.types.vip_url


class RealtimeEndpointInfo(TypedDict, closed=True):
    peak_requests_per_second: "capo_machine_learning.types.integer_type.IntegerType"
    """<p> The maximum processing rate for the real-time endpoint for <code>MLModel</code>, measured in incoming requests per second.</p>"""
    created_at: NotRequired["capo_machine_learning.types.epoch_time.EpochTime"]
    """<p>The time that the request to create the real-time endpoint for the <code>MLModel</code> was received. The time is expressed in epoch time.</p>"""
    endpoint_url: NotRequired["capo_machine_learning.types.vip_url.VipURL"]
    """<p>The URI that specifies where to send real-time prediction requests for the <code>MLModel</code>.</p> <p> <b>Note:</b> The application must wait until the real-time endpoint is ready before using this URI.</p>"""
    endpoint_status: NotRequired[
        "capo_machine_learning.types.realtime_endpoint_status.RealtimeEndpointStatus"
    ]
    """<p> The current status of the real-time endpoint for the <code>MLModel</code>. This element can have one of the following values: </p> <ul> <li> <p> <code>NONE</code> - Endpoint does not exist or was previously deleted.</p> </li> <li> <p> <code>READY</code> - Endpoint is ready to be used for real-time predictions.</p> </li> <li> <p> <code>UPDATING</code> - Updating/creating the endpoint. </p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RealtimeEndpointInfo) -> dict:
    out: dict = {}
    out["PeakRequestsPerSecond"] = value.get("peak_requests_per_second", 0)
    if "created_at" in value:
        import capo_machine_learning.types.epoch_time

        out["CreatedAt"] = (
            capo_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    if "endpoint_url" in value:
        out["EndpointUrl"] = value["endpoint_url"]
    if "endpoint_status" in value:
        import capo_machine_learning.types.realtime_endpoint_status

        out["EndpointStatus"] = (
            capo_machine_learning.types.realtime_endpoint_status.serialize_aws_json_1_1(
                value["endpoint_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RealtimeEndpointInfo:
    out: RealtimeEndpointInfo = {}  # type: ignore[typeddict-item]
    if "PeakRequestsPerSecond" in data:
        out["peak_requests_per_second"] = data["PeakRequestsPerSecond"]
    else:
        out["peak_requests_per_second"] = 0
    if "CreatedAt" in data:
        import capo_machine_learning.types.epoch_time

        out["created_at"] = (
            capo_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["CreatedAt"]
            )
        )
    if "EndpointUrl" in data:
        out["endpoint_url"] = data["EndpointUrl"]
    if "EndpointStatus" in data:
        import capo_machine_learning.types.realtime_endpoint_status

        out["endpoint_status"] = (
            capo_machine_learning.types.realtime_endpoint_status.deserialize_aws_json_1_1(
                data["EndpointStatus"]
            )
        )
    return out
