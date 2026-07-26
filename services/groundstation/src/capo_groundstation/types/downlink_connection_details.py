"""Generated from Smithy shape ``com.amazonaws.groundstation#DownlinkConnectionDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_groundstation.types.connection_details
    import capo_groundstation.types.ranged_connection_details


class DownlinkConnectionDetails(TypedDict, closed=True):
    agent_ip_and_port_address: (
        "capo_groundstation.types.ranged_connection_details.RangedConnectionDetails"
    )
    egress_address_and_port: (
        "capo_groundstation.types.connection_details.ConnectionDetails"
    )


# --- restJson1 ser/de ---
def serialize_json(value: DownlinkConnectionDetails) -> dict:
    out: dict = {}
    import capo_groundstation.types.ranged_connection_details

    out["agentIpAndPortAddress"] = (
        capo_groundstation.types.ranged_connection_details.serialize_json(
            value["agent_ip_and_port_address"]
        )
    )
    import capo_groundstation.types.connection_details

    out["egressAddressAndPort"] = (
        capo_groundstation.types.connection_details.serialize_json(
            value["egress_address_and_port"]
        )
    )
    return out


def deserialize_json(data: dict) -> DownlinkConnectionDetails:
    out: DownlinkConnectionDetails = {}  # type: ignore[typeddict-item]
    if "agentIpAndPortAddress" in data:
        import capo_groundstation.types.ranged_connection_details

        out["agent_ip_and_port_address"] = (
            capo_groundstation.types.ranged_connection_details.deserialize_json(
                data["agentIpAndPortAddress"]
            )
        )
    else:
        raise DeserializationError(
            "DownlinkConnectionDetails.agent_ip_and_port_address required"
        )
    if "egressAddressAndPort" in data:
        import capo_groundstation.types.connection_details

        out["egress_address_and_port"] = (
            capo_groundstation.types.connection_details.deserialize_json(
                data["egressAddressAndPort"]
            )
        )
    else:
        raise DeserializationError(
            "DownlinkConnectionDetails.egress_address_and_port required"
        )
    return out
