"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessEndpointCidrOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.modify_verified_access_endpoint_port_range_list


class ModifyVerifiedAccessEndpointCidrOptions(TypedDict, closed=True):
    port_ranges: NotRequired[
        "capo_ec2.types.modify_verified_access_endpoint_port_range_list.ModifyVerifiedAccessEndpointPortRangeList"
    ]
    """<p>The port ranges.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessEndpointCidrOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "port_ranges" in value:
        import capo_ec2.types.modify_verified_access_endpoint_port_range_list

        capo_ec2.types.modify_verified_access_endpoint_port_range_list.serialize_ec2_query(
            value["port_ranges"], pairs, f"{key_prefix}PortRange"
        )


def deserialize_ec2_query(el: Element) -> ModifyVerifiedAccessEndpointCidrOptions:
    out: ModifyVerifiedAccessEndpointCidrOptions = {}  # type: ignore[typeddict-item]
    if el.find("PortRange") is not None:
        import capo_ec2.types.modify_verified_access_endpoint_port_range_list

        out["port_ranges"] = (
            capo_ec2.types.modify_verified_access_endpoint_port_range_list.deserialize_ec2_query(
                el, "PortRange"
            )
        )
    return out
