"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StartFlowCaptureResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_network_firewall.types.flow_operation_id
    import aws_sdk_network_firewall.types.flow_operation_status
    import aws_sdk_network_firewall.types.resource_arn


class StartFlowCaptureResponse(TypedDict):
    firewall_arn: NotRequired["aws_sdk_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    flow_operation_id: NotRequired[
        "aws_sdk_network_firewall.types.flow_operation_id.FlowOperationId"
    ]
    """<p>A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.</p>"""
    flow_operation_status: NotRequired[
        "aws_sdk_network_firewall.types.flow_operation_status.FlowOperationStatus"
    ]
    """<p>Returns the status of the flow operation. This string is returned in the responses to start, list, and describe commands.</p> <p>If the status is <code>COMPLETED_WITH_ERRORS</code>, results may be returned with any number of <code>Flows</code> missing from the response. If the status is <code>FAILED</code>, <code>Flows</code> returned will be empty.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StartFlowCaptureResponse) -> dict:
    out: dict = {}
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    if "flow_operation_id" in value:
        out["FlowOperationId"] = value["flow_operation_id"]
    if "flow_operation_status" in value:
        import aws_sdk_network_firewall.types.flow_operation_status

        out["FlowOperationStatus"] = (
            aws_sdk_network_firewall.types.flow_operation_status.serialize_aws_json_1_0(
                value["flow_operation_status"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> StartFlowCaptureResponse:
    out: StartFlowCaptureResponse = {}  # type: ignore[typeddict-item]
    if "FirewallArn" in data:
        out["firewall_arn"] = data["FirewallArn"]
    if "FlowOperationId" in data:
        out["flow_operation_id"] = data["FlowOperationId"]
    if "FlowOperationStatus" in data:
        import aws_sdk_network_firewall.types.flow_operation_status

        out["flow_operation_status"] = (
            aws_sdk_network_firewall.types.flow_operation_status.deserialize_aws_json_1_0(
                data["FlowOperationStatus"]
            )
        )
    return out
