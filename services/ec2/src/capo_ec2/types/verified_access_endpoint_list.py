"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.verified_access_endpoint

VerifiedAccessEndpointList: TypeAlias = list[
    "capo_ec2.types.verified_access_endpoint.VerifiedAccessEndpoint"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessEndpointList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.verified_access_endpoint

        capo_ec2.types.verified_access_endpoint.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessEndpointList:
    import capo_ec2.types.verified_access_endpoint

    out: VerifiedAccessEndpointList = []
    for child in el.findall("item"):
        out.append(capo_ec2.types.verified_access_endpoint.deserialize_ec2_query(child))
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> VerifiedAccessEndpointList:
    import capo_ec2.types.verified_access_endpoint

    out: VerifiedAccessEndpointList = []
    for child in parent.findall(tag):
        out.append(capo_ec2.types.verified_access_endpoint.deserialize_ec2_query(child))
    return out
