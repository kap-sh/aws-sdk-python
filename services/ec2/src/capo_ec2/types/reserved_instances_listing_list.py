"""Generated from Smithy shape ``com.amazonaws.ec2#ReservedInstancesListingList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reserved_instances_listing

ReservedInstancesListingList: TypeAlias = list[
    "capo_ec2.types.reserved_instances_listing.ReservedInstancesListing"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ReservedInstancesListingList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.reserved_instances_listing

        capo_ec2.types.reserved_instances_listing.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> ReservedInstancesListingList:
    import capo_ec2.types.reserved_instances_listing

    out: ReservedInstancesListingList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.reserved_instances_listing.deserialize_ec2_query(child)
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> ReservedInstancesListingList:
    import capo_ec2.types.reserved_instances_listing

    out: ReservedInstancesListingList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.reserved_instances_listing.deserialize_ec2_query(child)
        )
    return out
