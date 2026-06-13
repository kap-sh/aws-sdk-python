"""Generated from Smithy shape ``com.amazonaws.groundstation#UplinkAwsGroundStationAgentEndpoint``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.safe_name
    import aws_sdk_groundstation.types.uplink_dataflow_details


class UplinkAwsGroundStationAgentEndpoint(TypedDict):
    name: "aws_sdk_groundstation.types.safe_name.SafeName"
    """<p>Uplink dataflow endpoint name</p>"""
    dataflow_details: (
        "aws_sdk_groundstation.types.uplink_dataflow_details.UplinkDataflowDetails"
    )
    """<p>Dataflow details for the uplink endpoint</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UplinkAwsGroundStationAgentEndpoint) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_groundstation.types.uplink_dataflow_details

    out["dataflowDetails"] = (
        aws_sdk_groundstation.types.uplink_dataflow_details.serialize_json(
            value["dataflow_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> UplinkAwsGroundStationAgentEndpoint:
    out: UplinkAwsGroundStationAgentEndpoint = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UplinkAwsGroundStationAgentEndpoint.name required")
    if "dataflowDetails" in data:
        import aws_sdk_groundstation.types.uplink_dataflow_details

        out["dataflow_details"] = (
            aws_sdk_groundstation.types.uplink_dataflow_details.deserialize_json(
                data["dataflowDetails"]
            )
        )
    else:
        raise DeserializationError(
            "UplinkAwsGroundStationAgentEndpoint.dataflow_details required"
        )
    return out
