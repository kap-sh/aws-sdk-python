"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeAvailabilityMonitorTestOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.availability_monitor_test_status
    import capo_storage_gateway.types.gateway_arn
    import capo_storage_gateway.types.time


class DescribeAvailabilityMonitorTestOutput(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]
    status: NotRequired[
        "capo_storage_gateway.types.availability_monitor_test_status.AvailabilityMonitorTestStatus"
    ]
    """<p>The status of the high availability monitoring test. If a test hasn't been performed, the value of this field is null.</p>"""
    start_time: NotRequired["capo_storage_gateway.types.time.Time"]
    """<p>The time the high availability monitoring test was started. If a test hasn't been performed, the value of this field is null.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAvailabilityMonitorTestOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    if "status" in value:
        import capo_storage_gateway.types.availability_monitor_test_status

        out["Status"] = (
            capo_storage_gateway.types.availability_monitor_test_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "start_time" in value:
        import capo_storage_gateway.types.time

        out["StartTime"] = capo_storage_gateway.types.time.serialize_aws_json_1_1(
            value["start_time"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAvailabilityMonitorTestOutput:
    out: DescribeAvailabilityMonitorTestOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    if "Status" in data:
        import capo_storage_gateway.types.availability_monitor_test_status

        out["status"] = (
            capo_storage_gateway.types.availability_monitor_test_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "StartTime" in data:
        import capo_storage_gateway.types.time

        out["start_time"] = capo_storage_gateway.types.time.deserialize_aws_json_1_1(
            data["StartTime"]
        )
    return out
