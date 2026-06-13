"""Generated from Smithy shape ``com.amazonaws.groundstation#DownlinkConnectionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.connection_details
    import aws_sdk_groundstation.types.ranged_connection_details


class DownlinkConnectionDetails(TypedDict):
    agent_ip_and_port_address: (
        "aws_sdk_groundstation.types.ranged_connection_details.RangedConnectionDetails"
    )
    egress_address_and_port: (
        "aws_sdk_groundstation.types.connection_details.ConnectionDetails"
    )


# --- restJson1 ser/de ---
def serialize_json(value: DownlinkConnectionDetails) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.ranged_connection_details

    out["agentIpAndPortAddress"] = (
        aws_sdk_groundstation.types.ranged_connection_details.serialize_json(
            value["agent_ip_and_port_address"]
        )
    )
    import aws_sdk_groundstation.types.connection_details

    out["egressAddressAndPort"] = (
        aws_sdk_groundstation.types.connection_details.serialize_json(
            value["egress_address_and_port"]
        )
    )
    return out


def deserialize_json(data: dict) -> DownlinkConnectionDetails:
    out: DownlinkConnectionDetails = {}  # type: ignore[typeddict-item]
    if "agentIpAndPortAddress" in data:
        import aws_sdk_groundstation.types.ranged_connection_details

        out["agent_ip_and_port_address"] = (
            aws_sdk_groundstation.types.ranged_connection_details.deserialize_json(
                data["agentIpAndPortAddress"]
            )
        )
    else:
        raise DeserializationError(
            "DownlinkConnectionDetails.agent_ip_and_port_address required"
        )
    if "egressAddressAndPort" in data:
        import aws_sdk_groundstation.types.connection_details

        out["egress_address_and_port"] = (
            aws_sdk_groundstation.types.connection_details.deserialize_json(
                data["egressAddressAndPort"]
            )
        )
    else:
        raise DeserializationError(
            "DownlinkConnectionDetails.egress_address_and_port required"
        )
    return out
