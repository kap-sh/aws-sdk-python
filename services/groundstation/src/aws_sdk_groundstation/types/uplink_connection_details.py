"""Generated from Smithy shape ``com.amazonaws.groundstation#UplinkConnectionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.connection_details
    import aws_sdk_groundstation.types.ranged_connection_details


class UplinkConnectionDetails(TypedDict):
    ingress_address_and_port: (
        "aws_sdk_groundstation.types.connection_details.ConnectionDetails"
    )
    agent_ip_and_port_address: (
        "aws_sdk_groundstation.types.ranged_connection_details.RangedConnectionDetails"
    )


# --- restJson1 ser/de ---
def serialize_json(value: UplinkConnectionDetails) -> dict:
    out: dict = {}
    import aws_sdk_groundstation.types.connection_details

    out["ingressAddressAndPort"] = (
        aws_sdk_groundstation.types.connection_details.serialize_json(
            value["ingress_address_and_port"]
        )
    )
    import aws_sdk_groundstation.types.ranged_connection_details

    out["agentIpAndPortAddress"] = (
        aws_sdk_groundstation.types.ranged_connection_details.serialize_json(
            value["agent_ip_and_port_address"]
        )
    )
    return out


def deserialize_json(data: dict) -> UplinkConnectionDetails:
    out: UplinkConnectionDetails = {}  # type: ignore[typeddict-item]
    if "ingressAddressAndPort" in data:
        import aws_sdk_groundstation.types.connection_details

        out["ingress_address_and_port"] = (
            aws_sdk_groundstation.types.connection_details.deserialize_json(
                data["ingressAddressAndPort"]
            )
        )
    else:
        raise DeserializationError(
            "UplinkConnectionDetails.ingress_address_and_port required"
        )
    if "agentIpAndPortAddress" in data:
        import aws_sdk_groundstation.types.ranged_connection_details

        out["agent_ip_and_port_address"] = (
            aws_sdk_groundstation.types.ranged_connection_details.deserialize_json(
                data["agentIpAndPortAddress"]
            )
        )
    else:
        raise DeserializationError(
            "UplinkConnectionDetails.agent_ip_and_port_address required"
        )
    return out
