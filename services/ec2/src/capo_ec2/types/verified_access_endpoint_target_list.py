"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessEndpointTargetList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.verified_access_endpoint_target

VerifiedAccessEndpointTargetList: TypeAlias = list[
    "capo_ec2.types.verified_access_endpoint_target.VerifiedAccessEndpointTarget"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessEndpointTargetList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.verified_access_endpoint_target

        capo_ec2.types.verified_access_endpoint_target.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessEndpointTargetList:
    import capo_ec2.types.verified_access_endpoint_target

    out: VerifiedAccessEndpointTargetList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.verified_access_endpoint_target.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> VerifiedAccessEndpointTargetList:
    import capo_ec2.types.verified_access_endpoint_target

    out: VerifiedAccessEndpointTargetList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.verified_access_endpoint_target.deserialize_ec2_query(child)
        )
    return out
