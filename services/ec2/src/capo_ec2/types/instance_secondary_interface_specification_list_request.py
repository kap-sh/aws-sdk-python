"""Generated from Smithy shape ``com.amazonaws.ec2#InstanceSecondaryInterfaceSpecificationListRequest``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.instance_secondary_interface_specification_request

InstanceSecondaryInterfaceSpecificationListRequest: TypeAlias = list[
    "capo_ec2.types.instance_secondary_interface_specification_request.InstanceSecondaryInterfaceSpecificationRequest"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: InstanceSecondaryInterfaceSpecificationListRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.instance_secondary_interface_specification_request

        capo_ec2.types.instance_secondary_interface_specification_request.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    el: Element,
) -> InstanceSecondaryInterfaceSpecificationListRequest:
    import capo_ec2.types.instance_secondary_interface_specification_request

    out: InstanceSecondaryInterfaceSpecificationListRequest = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.instance_secondary_interface_specification_request.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> InstanceSecondaryInterfaceSpecificationListRequest:
    import capo_ec2.types.instance_secondary_interface_specification_request

    out: InstanceSecondaryInterfaceSpecificationListRequest = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.instance_secondary_interface_specification_request.deserialize_ec2_query(
                child
            )
        )
    return out
