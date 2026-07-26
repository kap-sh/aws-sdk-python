"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrafficRoutingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.capacity_size
    import capo_sagemaker.types.traffic_routing_config_type
    import capo_sagemaker.types.wait_interval_in_seconds


class TrafficRoutingConfig(TypedDict, closed=True):
    type: NotRequired[
        "capo_sagemaker.types.traffic_routing_config_type.TrafficRoutingConfigType"
    ]
    """<p>Traffic routing strategy type.</p> <ul> <li> <p> <code>ALL_AT_ONCE</code>: Endpoint traffic shifts to the new fleet in a single step. </p> </li> <li> <p> <code>CANARY</code>: Endpoint traffic shifts to the new fleet in two steps. The first step is the canary, which is a small portion of the traffic. The second step is the remainder of the traffic. </p> </li> <li> <p> <code>LINEAR</code>: Endpoint traffic shifts to the new fleet in n steps of a configurable size. </p> </li> </ul>"""
    wait_interval_in_seconds: NotRequired[
        "capo_sagemaker.types.wait_interval_in_seconds.WaitIntervalInSeconds"
    ]
    """<p>The waiting time (in seconds) between incremental steps to turn on traffic on the new endpoint fleet.</p>"""
    canary_size: NotRequired["capo_sagemaker.types.capacity_size.CapacitySize"]
    """<p>Batch size for the first step to turn on traffic on the new endpoint fleet. <code>Value</code> must be less than or equal to 50% of the variant's total instance count.</p>"""
    linear_step_size: NotRequired["capo_sagemaker.types.capacity_size.CapacitySize"]
    """<p>Batch size for each step to turn on traffic on the new endpoint fleet. <code>Value</code> must be 10-50% of the variant's total instance count.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrafficRoutingConfig) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_sagemaker.types.traffic_routing_config_type

        out["Type"] = (
            capo_sagemaker.types.traffic_routing_config_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "wait_interval_in_seconds" in value:
        out["WaitIntervalInSeconds"] = value["wait_interval_in_seconds"]
    if "canary_size" in value:
        import capo_sagemaker.types.capacity_size

        out["CanarySize"] = capo_sagemaker.types.capacity_size.serialize_aws_json_1_1(
            value["canary_size"]
        )
    if "linear_step_size" in value:
        import capo_sagemaker.types.capacity_size

        out["LinearStepSize"] = (
            capo_sagemaker.types.capacity_size.serialize_aws_json_1_1(
                value["linear_step_size"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrafficRoutingConfig:
    out: TrafficRoutingConfig = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_sagemaker.types.traffic_routing_config_type

        out["type"] = (
            capo_sagemaker.types.traffic_routing_config_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if "WaitIntervalInSeconds" in data:
        out["wait_interval_in_seconds"] = data["WaitIntervalInSeconds"]
    if "CanarySize" in data:
        import capo_sagemaker.types.capacity_size

        out["canary_size"] = (
            capo_sagemaker.types.capacity_size.deserialize_aws_json_1_1(
                data["CanarySize"]
            )
        )
    if "LinearStepSize" in data:
        import capo_sagemaker.types.capacity_size

        out["linear_step_size"] = (
            capo_sagemaker.types.capacity_size.deserialize_aws_json_1_1(
                data["LinearStepSize"]
            )
        )
    return out
