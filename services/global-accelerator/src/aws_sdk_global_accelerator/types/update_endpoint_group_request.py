"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#UpdateEndpointGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_global_accelerator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_global_accelerator.types.endpoint_configurations
    import aws_sdk_global_accelerator.types.generic_string
    import aws_sdk_global_accelerator.types.health_check_interval_seconds
    import aws_sdk_global_accelerator.types.health_check_path
    import aws_sdk_global_accelerator.types.health_check_port
    import aws_sdk_global_accelerator.types.health_check_protocol
    import aws_sdk_global_accelerator.types.port_overrides
    import aws_sdk_global_accelerator.types.threshold_count
    import aws_sdk_global_accelerator.types.traffic_dial_percentage


class UpdateEndpointGroupRequest(TypedDict):
    endpoint_group_arn: "aws_sdk_global_accelerator.types.generic_string.GenericString"
    """<p>The Amazon Resource Name (ARN) of the endpoint group.</p>"""
    endpoint_configurations: NotRequired[
        "aws_sdk_global_accelerator.types.endpoint_configurations.EndpointConfigurations"
    ]
    """<p>The list of endpoint objects. A resource must be valid and active when you add it as an endpoint.</p>"""
    traffic_dial_percentage: NotRequired[
        "aws_sdk_global_accelerator.types.traffic_dial_percentage.TrafficDialPercentage"
    ]
    """<p>The percentage of traffic to send to an Amazon Web Services Region. Additional traffic is distributed to other endpoint groups for this listener. </p> <p>Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.</p> <p>The default value is 100.</p>"""
    health_check_port: NotRequired[
        "aws_sdk_global_accelerator.types.health_check_port.HealthCheckPort"
    ]
    """<p>The port that Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default port is the listener port that this endpoint group is associated with. If the listener port is a list of ports, Global Accelerator uses the first port in the list.</p>"""
    health_check_protocol: NotRequired[
        "aws_sdk_global_accelerator.types.health_check_protocol.HealthCheckProtocol"
    ]
    """<p>The protocol that Global Accelerator uses to check the health of endpoints that are part of this endpoint group. The default value is TCP.</p>"""
    health_check_path: NotRequired[
        "aws_sdk_global_accelerator.types.health_check_path.HealthCheckPath"
    ]
    """<p>If the protocol is HTTP/S, then this specifies the path that is the destination for health check targets. The default value is slash (/).</p>"""
    health_check_interval_seconds: NotRequired[
        "aws_sdk_global_accelerator.types.health_check_interval_seconds.HealthCheckIntervalSeconds"
    ]
    """<p>The time—10 seconds or 30 seconds—between each health check for an endpoint. The default value is 30.</p>"""
    threshold_count: NotRequired[
        "aws_sdk_global_accelerator.types.threshold_count.ThresholdCount"
    ]
    """<p>The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.</p>"""
    port_overrides: NotRequired[
        "aws_sdk_global_accelerator.types.port_overrides.PortOverrides"
    ]
    r"""<p>Override specific listener ports used to route traffic to endpoints that are part of this endpoint group. For example, you can create a port override in which the listener receives user traffic on ports 80 and 443, but your accelerator routes that traffic to ports 1080 and 1443, respectively, on the endpoints.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/global-accelerator/latest/dg/about-endpoint-groups-port-override.html\"> Overriding listener ports</a> in the <i>Global Accelerator Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateEndpointGroupRequest) -> dict:
    out: dict = {}
    out["EndpointGroupArn"] = value["endpoint_group_arn"]
    if "endpoint_configurations" in value:
        import aws_sdk_global_accelerator.types.endpoint_configurations

        out["EndpointConfigurations"] = (
            aws_sdk_global_accelerator.types.endpoint_configurations.serialize_aws_json_1_1(
                value["endpoint_configurations"]
            )
        )
    if "traffic_dial_percentage" in value:
        out["TrafficDialPercentage"] = value["traffic_dial_percentage"]
    if "health_check_port" in value:
        out["HealthCheckPort"] = value["health_check_port"]
    if "health_check_protocol" in value:
        import aws_sdk_global_accelerator.types.health_check_protocol

        out["HealthCheckProtocol"] = (
            aws_sdk_global_accelerator.types.health_check_protocol.serialize_aws_json_1_1(
                value["health_check_protocol"]
            )
        )
    if "health_check_path" in value:
        out["HealthCheckPath"] = value["health_check_path"]
    if "health_check_interval_seconds" in value:
        out["HealthCheckIntervalSeconds"] = value["health_check_interval_seconds"]
    if "threshold_count" in value:
        out["ThresholdCount"] = value["threshold_count"]
    if "port_overrides" in value:
        import aws_sdk_global_accelerator.types.port_overrides

        out["PortOverrides"] = (
            aws_sdk_global_accelerator.types.port_overrides.serialize_aws_json_1_1(
                value["port_overrides"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateEndpointGroupRequest:
    out: UpdateEndpointGroupRequest = {}  # type: ignore[typeddict-item]
    if "EndpointGroupArn" in data:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    else:
        raise DeserializationError(
            "UpdateEndpointGroupRequest.endpoint_group_arn required"
        )
    if "EndpointConfigurations" in data:
        import aws_sdk_global_accelerator.types.endpoint_configurations

        out["endpoint_configurations"] = (
            aws_sdk_global_accelerator.types.endpoint_configurations.deserialize_aws_json_1_1(
                data["EndpointConfigurations"]
            )
        )
    if "TrafficDialPercentage" in data:
        out["traffic_dial_percentage"] = data["TrafficDialPercentage"]
    if "HealthCheckPort" in data:
        out["health_check_port"] = data["HealthCheckPort"]
    if "HealthCheckProtocol" in data:
        import aws_sdk_global_accelerator.types.health_check_protocol

        out["health_check_protocol"] = (
            aws_sdk_global_accelerator.types.health_check_protocol.deserialize_aws_json_1_1(
                data["HealthCheckProtocol"]
            )
        )
    if "HealthCheckPath" in data:
        out["health_check_path"] = data["HealthCheckPath"]
    if "HealthCheckIntervalSeconds" in data:
        out["health_check_interval_seconds"] = data["HealthCheckIntervalSeconds"]
    if "ThresholdCount" in data:
        out["threshold_count"] = data["ThresholdCount"]
    if "PortOverrides" in data:
        import aws_sdk_global_accelerator.types.port_overrides

        out["port_overrides"] = (
            aws_sdk_global_accelerator.types.port_overrides.deserialize_aws_json_1_1(
                data["PortOverrides"]
            )
        )
    return out
