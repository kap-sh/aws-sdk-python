"""Generated from Smithy shape ``com.amazonaws.groundstation#EndpointDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.aws_ground_station_agent_endpoint
    import aws_sdk_groundstation.types.capability_health
    import aws_sdk_groundstation.types.capability_health_reason_list
    import aws_sdk_groundstation.types.dataflow_endpoint
    import aws_sdk_groundstation.types.downlink_aws_ground_station_agent_endpoint_details
    import aws_sdk_groundstation.types.security_details
    import aws_sdk_groundstation.types.uplink_aws_ground_station_agent_endpoint_details


class EndpointDetails(TypedDict):
    security_details: NotRequired[
        "aws_sdk_groundstation.types.security_details.SecurityDetails"
    ]
    """<p>Endpoint security details including a list of subnets, a list of security groups and a role to connect streams to instances.</p>"""
    endpoint: NotRequired[
        "aws_sdk_groundstation.types.dataflow_endpoint.DataflowEndpoint"
    ]
    """<p>A dataflow endpoint.</p>"""
    aws_ground_station_agent_endpoint: NotRequired[
        "aws_sdk_groundstation.types.aws_ground_station_agent_endpoint.AwsGroundStationAgentEndpoint"
    ]
    """<p>An agent endpoint.</p>"""
    uplink_aws_ground_station_agent_endpoint: NotRequired[
        "aws_sdk_groundstation.types.uplink_aws_ground_station_agent_endpoint_details.UplinkAwsGroundStationAgentEndpointDetails"
    ]
    """<p>Definition for an uplink agent endpoint</p>"""
    downlink_aws_ground_station_agent_endpoint: NotRequired[
        "aws_sdk_groundstation.types.downlink_aws_ground_station_agent_endpoint_details.DownlinkAwsGroundStationAgentEndpointDetails"
    ]
    """<p>Definition for a downlink agent endpoint</p>"""
    health_status: NotRequired[
        "aws_sdk_groundstation.types.capability_health.CapabilityHealth"
    ]
    """<p>A dataflow endpoint health status. This field is ignored when calling <code>CreateDataflowEndpointGroup</code>.</p>"""
    health_reasons: NotRequired[
        "aws_sdk_groundstation.types.capability_health_reason_list.CapabilityHealthReasonList"
    ]
    """<p>Health reasons for a dataflow endpoint. This field is ignored when calling <code>CreateDataflowEndpointGroup</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EndpointDetails) -> dict:
    out: dict = {}
    if "security_details" in value:
        import aws_sdk_groundstation.types.security_details

        out["securityDetails"] = (
            aws_sdk_groundstation.types.security_details.serialize_json(
                value["security_details"]
            )
        )
    if "endpoint" in value:
        import aws_sdk_groundstation.types.dataflow_endpoint

        out["endpoint"] = aws_sdk_groundstation.types.dataflow_endpoint.serialize_json(
            value["endpoint"]
        )
    if "aws_ground_station_agent_endpoint" in value:
        import aws_sdk_groundstation.types.aws_ground_station_agent_endpoint

        out["awsGroundStationAgentEndpoint"] = (
            aws_sdk_groundstation.types.aws_ground_station_agent_endpoint.serialize_json(
                value["aws_ground_station_agent_endpoint"]
            )
        )
    if "uplink_aws_ground_station_agent_endpoint" in value:
        import aws_sdk_groundstation.types.uplink_aws_ground_station_agent_endpoint_details

        out["uplinkAwsGroundStationAgentEndpoint"] = (
            aws_sdk_groundstation.types.uplink_aws_ground_station_agent_endpoint_details.serialize_json(
                value["uplink_aws_ground_station_agent_endpoint"]
            )
        )
    if "downlink_aws_ground_station_agent_endpoint" in value:
        import aws_sdk_groundstation.types.downlink_aws_ground_station_agent_endpoint_details

        out["downlinkAwsGroundStationAgentEndpoint"] = (
            aws_sdk_groundstation.types.downlink_aws_ground_station_agent_endpoint_details.serialize_json(
                value["downlink_aws_ground_station_agent_endpoint"]
            )
        )
    if "health_status" in value:
        import aws_sdk_groundstation.types.capability_health

        out["healthStatus"] = (
            aws_sdk_groundstation.types.capability_health.serialize_json(
                value["health_status"]
            )
        )
    if "health_reasons" in value:
        import aws_sdk_groundstation.types.capability_health_reason_list

        out["healthReasons"] = (
            aws_sdk_groundstation.types.capability_health_reason_list.serialize_json(
                value["health_reasons"]
            )
        )
    return out


def deserialize_json(data: dict) -> EndpointDetails:
    out: EndpointDetails = {}  # type: ignore[typeddict-item]
    if "securityDetails" in data:
        import aws_sdk_groundstation.types.security_details

        out["security_details"] = (
            aws_sdk_groundstation.types.security_details.deserialize_json(
                data["securityDetails"]
            )
        )
    if "endpoint" in data:
        import aws_sdk_groundstation.types.dataflow_endpoint

        out["endpoint"] = (
            aws_sdk_groundstation.types.dataflow_endpoint.deserialize_json(
                data["endpoint"]
            )
        )
    if "awsGroundStationAgentEndpoint" in data:
        import aws_sdk_groundstation.types.aws_ground_station_agent_endpoint

        out["aws_ground_station_agent_endpoint"] = (
            aws_sdk_groundstation.types.aws_ground_station_agent_endpoint.deserialize_json(
                data["awsGroundStationAgentEndpoint"]
            )
        )
    if "uplinkAwsGroundStationAgentEndpoint" in data:
        import aws_sdk_groundstation.types.uplink_aws_ground_station_agent_endpoint_details

        out["uplink_aws_ground_station_agent_endpoint"] = (
            aws_sdk_groundstation.types.uplink_aws_ground_station_agent_endpoint_details.deserialize_json(
                data["uplinkAwsGroundStationAgentEndpoint"]
            )
        )
    if "downlinkAwsGroundStationAgentEndpoint" in data:
        import aws_sdk_groundstation.types.downlink_aws_ground_station_agent_endpoint_details

        out["downlink_aws_ground_station_agent_endpoint"] = (
            aws_sdk_groundstation.types.downlink_aws_ground_station_agent_endpoint_details.deserialize_json(
                data["downlinkAwsGroundStationAgentEndpoint"]
            )
        )
    if "healthStatus" in data:
        import aws_sdk_groundstation.types.capability_health

        out["health_status"] = (
            aws_sdk_groundstation.types.capability_health.deserialize_json(
                data["healthStatus"]
            )
        )
    if "healthReasons" in data:
        import aws_sdk_groundstation.types.capability_health_reason_list

        out["health_reasons"] = (
            aws_sdk_groundstation.types.capability_health_reason_list.deserialize_json(
                data["healthReasons"]
            )
        )
    return out
