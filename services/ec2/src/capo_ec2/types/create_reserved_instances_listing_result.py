"""Generated from Smithy shape ``com.amazonaws.ec2#CreateReservedInstancesListingResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.reserved_instances_listing_list


class CreateReservedInstancesListingResult(TypedDict, closed=True):
    reserved_instances_listings: NotRequired[
        "capo_ec2.types.reserved_instances_listing_list.ReservedInstancesListingList"
    ]
    """<p>Information about the Standard Reserved Instance listing.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateReservedInstancesListingResult,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "reserved_instances_listings" in value:
        import capo_ec2.types.reserved_instances_listing_list

        capo_ec2.types.reserved_instances_listing_list.serialize_ec2_query(
            value["reserved_instances_listings"],
            pairs,
            f"{key_prefix}ReservedInstancesListingsSet",
        )


def deserialize_ec2_query(el: Element) -> CreateReservedInstancesListingResult:
    out: CreateReservedInstancesListingResult = {}  # type: ignore[typeddict-item]
    if el.find("ReservedInstancesListingsSet") is not None:
        import capo_ec2.types.reserved_instances_listing_list

        out["reserved_instances_listings"] = (
            capo_ec2.types.reserved_instances_listing_list.deserialize_ec2_query(
                el, "ReservedInstancesListingsSet"
            )
        )
    return out
