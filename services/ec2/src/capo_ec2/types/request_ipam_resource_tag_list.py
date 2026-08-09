"""Generated from Smithy shape ``com.amazonaws.ec2#RequestIpamResourceTagList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.request_ipam_resource_tag

RequestIpamResourceTagList: TypeAlias = list[
    "capo_ec2.types.request_ipam_resource_tag.RequestIpamResourceTag"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: RequestIpamResourceTagList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.request_ipam_resource_tag

        capo_ec2.types.request_ipam_resource_tag.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> RequestIpamResourceTagList:
    import capo_ec2.types.request_ipam_resource_tag

    out: RequestIpamResourceTagList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.request_ipam_resource_tag.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(parent: Element, tag: str) -> RequestIpamResourceTagList:
    import capo_ec2.types.request_ipam_resource_tag

    out: RequestIpamResourceTagList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.request_ipam_resource_tag.deserialize_ec2_query(child)
        )
    return out
