"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#EndpointGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_global_accelerator.types.endpoint_descriptions
    import capo_global_accelerator.types.generic_string
    import capo_global_accelerator.types.health_check_interval_seconds
    import capo_global_accelerator.types.health_check_path
    import capo_global_accelerator.types.health_check_port
    import capo_global_accelerator.types.health_check_protocol
    import capo_global_accelerator.types.port_overrides
    import capo_global_accelerator.types.threshold_count
    import capo_global_accelerator.types.traffic_dial_percentage


class EndpointGroup(TypedDict, closed=True):
    endpoint_group_arn: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Resource Name (ARN) of the endpoint group.</p>"""
    endpoint_group_region: NotRequired[
        "capo_global_accelerator.types.generic_string.GenericString"
    ]
    """<p>The Amazon Web Services Region where the endpoint group is located.</p>"""
    endpoint_descriptions: NotRequired[
        "capo_global_accelerator.types.endpoint_descriptions.EndpointDescriptions"
    ]
    """<p>The list of endpoint objects.</p>"""
    traffic_dial_percentage: NotRequired[
        "capo_global_accelerator.types.traffic_dial_percentage.TrafficDialPercentage"
    ]
    """<p>The percentage of traffic to send to an Amazon Web Services Region. Additional traffic is distributed to other endpoint groups for this listener. </p> <p>Use this action to increase (dial up) or decrease (dial down) traffic to a specific Region. The percentage is applied to the traffic that would otherwise have been routed to the Region based on optimal routing.</p> <p>The default value is 100.</p>"""
    health_check_port: NotRequired[
        "capo_global_accelerator.types.health_check_port.HealthCheckPort"
    ]
    """<p>The port that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. </p> <p>The default port is the port for the listener that this endpoint group is associated with. If the listener port is a list, Global Accelerator uses the first specified port in the list of ports.</p>"""
    health_check_protocol: NotRequired[
        "capo_global_accelerator.types.health_check_protocol.HealthCheckProtocol"
    ]
    """<p>The protocol that Global Accelerator uses to perform health checks on endpoints that are part of this endpoint group. The default value is TCP.</p>"""
    health_check_path: NotRequired[
        "capo_global_accelerator.types.health_check_path.HealthCheckPath"
    ]
    """<p>If the protocol is HTTP/S, then this value provides the ping path that Global Accelerator uses for the destination on the endpoints for health checks. The default is slash (/).</p>"""
    health_check_interval_seconds: NotRequired[
        "capo_global_accelerator.types.health_check_interval_seconds.HealthCheckIntervalSeconds"
    ]
    """<p>The time—10 seconds or 30 seconds—between health checks for each endpoint. The default value is 30.</p>"""
    threshold_count: NotRequired[
        "capo_global_accelerator.types.threshold_count.ThresholdCount"
    ]
    """<p>The number of consecutive health checks required to set the state of a healthy endpoint to unhealthy, or to set an unhealthy endpoint to healthy. The default value is 3.</p>"""
    port_overrides: NotRequired[
        "capo_global_accelerator.types.port_overrides.PortOverrides"
    ]
    """<p>Allows you to override the destination ports used to route traffic to an endpoint. Using a port override lets you map a list of external destination ports (that your users send traffic to) to a list of internal destination ports that you want an application endpoint to receive traffic on. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EndpointGroup) -> dict:
    out: dict = {}
    if "endpoint_group_arn" in value:
        out["EndpointGroupArn"] = value["endpoint_group_arn"]
    if "endpoint_group_region" in value:
        out["EndpointGroupRegion"] = value["endpoint_group_region"]
    if "endpoint_descriptions" in value:
        import capo_global_accelerator.types.endpoint_descriptions

        out["EndpointDescriptions"] = (
            capo_global_accelerator.types.endpoint_descriptions.serialize_aws_json_1_1(
                value["endpoint_descriptions"]
            )
        )
    if "traffic_dial_percentage" in value:
        out["TrafficDialPercentage"] = value["traffic_dial_percentage"]
    if "health_check_port" in value:
        out["HealthCheckPort"] = value["health_check_port"]
    if "health_check_protocol" in value:
        import capo_global_accelerator.types.health_check_protocol

        out["HealthCheckProtocol"] = (
            capo_global_accelerator.types.health_check_protocol.serialize_aws_json_1_1(
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
        import capo_global_accelerator.types.port_overrides

        out["PortOverrides"] = (
            capo_global_accelerator.types.port_overrides.serialize_aws_json_1_1(
                value["port_overrides"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EndpointGroup:
    out: EndpointGroup = {}  # type: ignore[typeddict-item]
    if "EndpointGroupArn" in data:
        out["endpoint_group_arn"] = data["EndpointGroupArn"]
    if "EndpointGroupRegion" in data:
        out["endpoint_group_region"] = data["EndpointGroupRegion"]
    if "EndpointDescriptions" in data:
        import capo_global_accelerator.types.endpoint_descriptions

        out["endpoint_descriptions"] = (
            capo_global_accelerator.types.endpoint_descriptions.deserialize_aws_json_1_1(
                data["EndpointDescriptions"]
            )
        )
    if "TrafficDialPercentage" in data:
        out["traffic_dial_percentage"] = data["TrafficDialPercentage"]
    if "HealthCheckPort" in data:
        out["health_check_port"] = data["HealthCheckPort"]
    if "HealthCheckProtocol" in data:
        import capo_global_accelerator.types.health_check_protocol

        out["health_check_protocol"] = (
            capo_global_accelerator.types.health_check_protocol.deserialize_aws_json_1_1(
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
        import capo_global_accelerator.types.port_overrides

        out["port_overrides"] = (
            capo_global_accelerator.types.port_overrides.deserialize_aws_json_1_1(
                data["PortOverrides"]
            )
        )
    return out
