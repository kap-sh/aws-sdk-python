"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkEdge``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.constrained_string_list
    import aws_sdk_networkmanager.types.external_region_code
    import aws_sdk_networkmanager.types.long


class CoreNetworkEdge(TypedDict):
    edge_location: NotRequired[
        "aws_sdk_networkmanager.types.external_region_code.ExternalRegionCode"
    ]
    """<p>The Region where a core network edge is located.</p>"""
    asn: NotRequired["aws_sdk_networkmanager.types.long.Long"]
    """<p>The ASN of a core network edge.</p>"""
    inside_cidr_blocks: NotRequired[
        "aws_sdk_networkmanager.types.constrained_string_list.ConstrainedStringList"
    ]
    """<p>The inside IP addresses used for core network edges.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkEdge) -> dict:
    out: dict = {}
    if "edge_location" in value:
        out["EdgeLocation"] = value["edge_location"]
    if "asn" in value:
        out["Asn"] = value["asn"]
    if "inside_cidr_blocks" in value:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["InsideCidrBlocks"] = (
            aws_sdk_networkmanager.types.constrained_string_list.serialize_json(
                value["inside_cidr_blocks"]
            )
        )
    return out


def deserialize_json(data: dict) -> CoreNetworkEdge:
    out: CoreNetworkEdge = {}  # type: ignore[typeddict-item]
    if "EdgeLocation" in data:
        out["edge_location"] = data["EdgeLocation"]
    if "Asn" in data:
        out["asn"] = data["Asn"]
    if "InsideCidrBlocks" in data:
        import aws_sdk_networkmanager.types.constrained_string_list

        out["inside_cidr_blocks"] = (
            aws_sdk_networkmanager.types.constrained_string_list.deserialize_json(
                data["InsideCidrBlocks"]
            )
        )
    return out
