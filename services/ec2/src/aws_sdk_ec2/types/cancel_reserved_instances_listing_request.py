"""Generated from Smithy shape ``com.amazonaws.ec2#CancelReservedInstancesListingRequest``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.reserved_instances_listing_id


class CancelReservedInstancesListingRequest(TypedDict):
    reserved_instances_listing_id: NotRequired[
        "aws_sdk_ec2.types.reserved_instances_listing_id.ReservedInstancesListingId"
    ]
    """<p>The ID of the Reserved Instance listing.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelReservedInstancesListingRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    if "reserved_instances_listing_id" in value:
        pairs.append(
            (
                f"{prefix}.ReservedInstancesListingId",
                str(value["reserved_instances_listing_id"]),
            )
        )


def deserialize_ec2_query(el: Element) -> CancelReservedInstancesListingRequest:
    out: CancelReservedInstancesListingRequest = {}  # type: ignore[typeddict-item]
    child_reserved_instances_listing_id = el.find("ReservedInstancesListingId")
    if child_reserved_instances_listing_id is not None:
        out["reserved_instances_listing_id"] = str(
            child_reserved_instances_listing_id.text or ""
        )
    return out
