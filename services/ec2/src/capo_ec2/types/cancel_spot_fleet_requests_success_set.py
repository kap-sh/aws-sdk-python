"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsSuccessSet``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.cancel_spot_fleet_requests_success_item

CancelSpotFleetRequestsSuccessSet: TypeAlias = list[
    "capo_ec2.types.cancel_spot_fleet_requests_success_item.CancelSpotFleetRequestsSuccessItem"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelSpotFleetRequestsSuccessSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import capo_ec2.types.cancel_spot_fleet_requests_success_item

        capo_ec2.types.cancel_spot_fleet_requests_success_item.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> CancelSpotFleetRequestsSuccessSet:
    import capo_ec2.types.cancel_spot_fleet_requests_success_item

    out: CancelSpotFleetRequestsSuccessSet = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.cancel_spot_fleet_requests_success_item.deserialize_ec2_query(
                child
            )
        )
    return out
