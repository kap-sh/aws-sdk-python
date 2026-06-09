"""Generated from Smithy shape ``com.amazonaws.ec2#CancelSpotFleetRequestsErrorSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.cancel_spot_fleet_requests_error_item

CancelSpotFleetRequestsErrorSet: TypeAlias = list[
    "aws_sdk_ec2.types.cancel_spot_fleet_requests_error_item.CancelSpotFleetRequestsErrorItem"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CancelSpotFleetRequestsErrorSet, pairs: list[tuple[str, str]], prefix: str
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.cancel_spot_fleet_requests_error_item

        aws_sdk_ec2.types.cancel_spot_fleet_requests_error_item.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(parent: Element, tag: str) -> CancelSpotFleetRequestsErrorSet:
    import aws_sdk_ec2.types.cancel_spot_fleet_requests_error_item

    out: CancelSpotFleetRequestsErrorSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.cancel_spot_fleet_requests_error_item.deserialize_ec2_query(
                child
            )
        )
    return out
