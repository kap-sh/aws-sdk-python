"""Generated from Smithy shape ``com.amazonaws.groundstation#CreateEndpointDetails``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_groundstation.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.downlink_aws_ground_station_agent_endpoint
    import aws_sdk_groundstation.types.uplink_aws_ground_station_agent_endpoint


class _CreateEndpointDetails_uplinkAwsGroundStationAgentEndpoint(TypedDict):
    uplinkAwsGroundStationAgentEndpoint: "aws_sdk_groundstation.types.uplink_aws_ground_station_agent_endpoint.UplinkAwsGroundStationAgentEndpoint"


class _CreateEndpointDetails_downlinkAwsGroundStationAgentEndpoint(TypedDict):
    downlinkAwsGroundStationAgentEndpoint: "aws_sdk_groundstation.types.downlink_aws_ground_station_agent_endpoint.DownlinkAwsGroundStationAgentEndpoint"


CreateEndpointDetails: TypeAlias = (
    _CreateEndpointDetails_uplinkAwsGroundStationAgentEndpoint
    | _CreateEndpointDetails_downlinkAwsGroundStationAgentEndpoint
)


# --- restJson1 ser/de ---
def serialize_json(value: CreateEndpointDetails) -> dict:
    if "uplinkAwsGroundStationAgentEndpoint" in value:
        import aws_sdk_groundstation.types.uplink_aws_ground_station_agent_endpoint

        return {
            "uplinkAwsGroundStationAgentEndpoint": aws_sdk_groundstation.types.uplink_aws_ground_station_agent_endpoint.serialize_json(
                value["uplinkAwsGroundStationAgentEndpoint"]
            )
        }
    elif "downlinkAwsGroundStationAgentEndpoint" in value:
        import aws_sdk_groundstation.types.downlink_aws_ground_station_agent_endpoint

        return {
            "downlinkAwsGroundStationAgentEndpoint": aws_sdk_groundstation.types.downlink_aws_ground_station_agent_endpoint.serialize_json(
                value["downlinkAwsGroundStationAgentEndpoint"]
            )
        }
    else:
        raise SerializationError("CreateEndpointDetails: no variant present")


def deserialize_json(data: dict) -> CreateEndpointDetails:
    if "uplinkAwsGroundStationAgentEndpoint" in data:
        import aws_sdk_groundstation.types.uplink_aws_ground_station_agent_endpoint

        return {
            "uplinkAwsGroundStationAgentEndpoint": aws_sdk_groundstation.types.uplink_aws_ground_station_agent_endpoint.deserialize_json(
                data["uplinkAwsGroundStationAgentEndpoint"]
            )
        }
    elif "downlinkAwsGroundStationAgentEndpoint" in data:
        import aws_sdk_groundstation.types.downlink_aws_ground_station_agent_endpoint

        return {
            "downlinkAwsGroundStationAgentEndpoint": aws_sdk_groundstation.types.downlink_aws_ground_station_agent_endpoint.deserialize_json(
                data["downlinkAwsGroundStationAgentEndpoint"]
            )
        }
    else:
        raise DeserializationError("CreateEndpointDetails: no recognized variant key")
