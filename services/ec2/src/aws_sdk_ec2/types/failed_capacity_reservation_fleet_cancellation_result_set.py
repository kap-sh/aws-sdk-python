"""Generated from Smithy shape ``com.amazonaws.ec2#FailedCapacityReservationFleetCancellationResultSet``."""

from typing import TYPE_CHECKING, TypeAlias

from aws_sdk_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result

FailedCapacityReservationFleetCancellationResultSet: TypeAlias = list[
    "aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result.FailedCapacityReservationFleetCancellationResult"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FailedCapacityReservationFleetCancellationResultSet,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    for n, item in enumerate(value, 1):
        import aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result

        aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(
    parent: Element, tag: str
) -> FailedCapacityReservationFleetCancellationResultSet:
    import aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result

    out: FailedCapacityReservationFleetCancellationResultSet = []
    for child in parent.findall(tag):
        out.append(
            aws_sdk_ec2.types.failed_capacity_reservation_fleet_cancellation_result.deserialize_ec2_query(
                child
            )
        )
    return out
