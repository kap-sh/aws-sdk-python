"""Generated from Smithy shape ``com.amazonaws.groundstation#DownlinkAwsGroundStationAgentEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.downlink_dataflow_details
    import aws_sdk_groundstation.types.safe_name


class DownlinkAwsGroundStationAgentEndpoint(TypedDict, closed=True):
    name: "aws_sdk_groundstation.types.safe_name.SafeName"
    """<p>Downlink dataflow endpoint name</p>"""
    dataflow_details: (
        "aws_sdk_groundstation.types.downlink_dataflow_details.DownlinkDataflowDetails"
    )
    """<p>Dataflow details for the downlink endpoint</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DownlinkAwsGroundStationAgentEndpoint) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_groundstation.types.downlink_dataflow_details

    out["dataflowDetails"] = (
        aws_sdk_groundstation.types.downlink_dataflow_details.serialize_json(
            value["dataflow_details"]
        )
    )
    return out


def deserialize_json(data: dict) -> DownlinkAwsGroundStationAgentEndpoint:
    out: DownlinkAwsGroundStationAgentEndpoint = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "DownlinkAwsGroundStationAgentEndpoint.name required"
        )
    if "dataflowDetails" in data:
        import aws_sdk_groundstation.types.downlink_dataflow_details

        out["dataflow_details"] = (
            aws_sdk_groundstation.types.downlink_dataflow_details.deserialize_json(
                data["dataflowDetails"]
            )
        )
    else:
        raise DeserializationError(
            "DownlinkAwsGroundStationAgentEndpoint.dataflow_details required"
        )
    return out
