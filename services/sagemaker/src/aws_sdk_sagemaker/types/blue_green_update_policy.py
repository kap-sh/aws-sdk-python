"""Generated from Smithy shape ``com.amazonaws.sagemaker#BlueGreenUpdatePolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.maximum_execution_timeout_in_seconds
    import aws_sdk_sagemaker.types.termination_wait_in_seconds
    import aws_sdk_sagemaker.types.traffic_routing_config


class BlueGreenUpdatePolicy(TypedDict, closed=True):
    traffic_routing_configuration: NotRequired[
        "aws_sdk_sagemaker.types.traffic_routing_config.TrafficRoutingConfig"
    ]
    """<p>Defines the traffic routing strategy to shift traffic from the old fleet to the new fleet during an endpoint deployment.</p>"""
    termination_wait_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.termination_wait_in_seconds.TerminationWaitInSeconds"
    ]
    """<p>Additional waiting time in seconds after the completion of an endpoint deployment before terminating the old endpoint fleet. Default is 0.</p>"""
    maximum_execution_timeout_in_seconds: NotRequired[
        "aws_sdk_sagemaker.types.maximum_execution_timeout_in_seconds.MaximumExecutionTimeoutInSeconds"
    ]
    """<p>Maximum execution timeout for the deployment. Note that the timeout value should be larger than the total waiting time specified in <code>TerminationWaitInSeconds</code> and <code>WaitIntervalInSeconds</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlueGreenUpdatePolicy) -> dict:
    out: dict = {}
    if "traffic_routing_configuration" in value:
        import aws_sdk_sagemaker.types.traffic_routing_config

        out["TrafficRoutingConfiguration"] = (
            aws_sdk_sagemaker.types.traffic_routing_config.serialize_aws_json_1_1(
                value["traffic_routing_configuration"]
            )
        )
    if "termination_wait_in_seconds" in value:
        out["TerminationWaitInSeconds"] = value["termination_wait_in_seconds"]
    if "maximum_execution_timeout_in_seconds" in value:
        out["MaximumExecutionTimeoutInSeconds"] = value[
            "maximum_execution_timeout_in_seconds"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> BlueGreenUpdatePolicy:
    out: BlueGreenUpdatePolicy = {}  # type: ignore[typeddict-item]
    if "TrafficRoutingConfiguration" in data:
        import aws_sdk_sagemaker.types.traffic_routing_config

        out["traffic_routing_configuration"] = (
            aws_sdk_sagemaker.types.traffic_routing_config.deserialize_aws_json_1_1(
                data["TrafficRoutingConfiguration"]
            )
        )
    if "TerminationWaitInSeconds" in data:
        out["termination_wait_in_seconds"] = data["TerminationWaitInSeconds"]
    if "MaximumExecutionTimeoutInSeconds" in data:
        out["maximum_execution_timeout_in_seconds"] = data[
            "MaximumExecutionTimeoutInSeconds"
        ]
    return out
