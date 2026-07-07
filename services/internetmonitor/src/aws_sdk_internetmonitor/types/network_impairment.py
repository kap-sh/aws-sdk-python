"""Generated from Smithy shape ``com.amazonaws.internetmonitor#NetworkImpairment``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_internetmonitor.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_internetmonitor.types.network_list
    import aws_sdk_internetmonitor.types.triangulation_event_type


class NetworkImpairment(TypedDict, closed=True):
    networks: "aws_sdk_internetmonitor.types.network_list.NetworkList"
    """<p>The networks that could be impacted by a network impairment event.</p>"""
    as_path: "aws_sdk_internetmonitor.types.network_list.NetworkList"
    """<p>The combination of the Autonomous System Number (ASN) of the network and the name of the network.</p>"""
    network_event_type: (
        "aws_sdk_internetmonitor.types.triangulation_event_type.TriangulationEventType"
    )
    """<p>The type of network impairment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkImpairment) -> dict:
    out: dict = {}
    import aws_sdk_internetmonitor.types.network_list

    out["Networks"] = aws_sdk_internetmonitor.types.network_list.serialize_json(
        value["networks"]
    )
    import aws_sdk_internetmonitor.types.network_list

    out["AsPath"] = aws_sdk_internetmonitor.types.network_list.serialize_json(
        value["as_path"]
    )
    out["NetworkEventType"] = value["network_event_type"]
    return out


def deserialize_json(data: dict) -> NetworkImpairment:
    out: NetworkImpairment = {}  # type: ignore[typeddict-item]
    if "Networks" in data:
        import aws_sdk_internetmonitor.types.network_list

        out["networks"] = aws_sdk_internetmonitor.types.network_list.deserialize_json(
            data["Networks"]
        )
    else:
        raise DeserializationError("NetworkImpairment.networks required")
    if "AsPath" in data:
        import aws_sdk_internetmonitor.types.network_list

        out["as_path"] = aws_sdk_internetmonitor.types.network_list.deserialize_json(
            data["AsPath"]
        )
    else:
        raise DeserializationError("NetworkImpairment.as_path required")
    if "NetworkEventType" in data:
        out["network_event_type"] = data["NetworkEventType"]
    else:
        raise DeserializationError("NetworkImpairment.network_event_type required")
    return out
