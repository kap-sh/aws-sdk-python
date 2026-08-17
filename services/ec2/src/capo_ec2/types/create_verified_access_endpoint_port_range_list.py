"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVerifiedAccessEndpointPortRangeList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.create_verified_access_endpoint_port_range

CreateVerifiedAccessEndpointPortRangeList: TypeAlias = list[
    "capo_ec2.types.create_verified_access_endpoint_port_range.CreateVerifiedAccessEndpointPortRange"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVerifiedAccessEndpointPortRangeList,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.create_verified_access_endpoint_port_range

        capo_ec2.types.create_verified_access_endpoint_port_range.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> CreateVerifiedAccessEndpointPortRangeList:
    import capo_ec2.types.create_verified_access_endpoint_port_range

    out: CreateVerifiedAccessEndpointPortRangeList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.create_verified_access_endpoint_port_range.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> CreateVerifiedAccessEndpointPortRangeList:
    import capo_ec2.types.create_verified_access_endpoint_port_range

    out: CreateVerifiedAccessEndpointPortRangeList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.create_verified_access_endpoint_port_range.deserialize_ec2_query(
                child
            )
        )
    return out
