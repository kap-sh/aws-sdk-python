"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessEndpointCidrOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.modify_verified_access_endpoint_port_range_list


class ModifyVerifiedAccessEndpointCidrOptions(TypedDict):
    port_ranges: NotRequired[
        "aws_sdk_ec2.types.modify_verified_access_endpoint_port_range_list.ModifyVerifiedAccessEndpointPortRangeList"
    ]
    """<p>The port ranges.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessEndpointCidrOptions,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "port_ranges" in value:
        import aws_sdk_ec2.types.modify_verified_access_endpoint_port_range_list

        aws_sdk_ec2.types.modify_verified_access_endpoint_port_range_list.serialize_ec2_query(
            value["port_ranges"], pairs, f"{prefix}.PortRanges"
        )


def deserialize_ec2_query(el: Element) -> ModifyVerifiedAccessEndpointCidrOptions:
    out: ModifyVerifiedAccessEndpointCidrOptions = {}  # type: ignore[typeddict-item]
    if el.find("PortRanges") is not None:
        import aws_sdk_ec2.types.modify_verified_access_endpoint_port_range_list

        out["port_ranges"] = (
            aws_sdk_ec2.types.modify_verified_access_endpoint_port_range_list.deserialize_ec2_query(
                el, "PortRanges"
            )
        )
    return out
