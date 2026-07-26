"""Generated from Smithy shape ``com.amazonaws.sagemaker#Ec2CapacityReservationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.ec2_capacity_reservation

Ec2CapacityReservationsList: TypeAlias = list[
    "capo_sagemaker.types.ec2_capacity_reservation.Ec2CapacityReservation"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ec2CapacityReservationsList) -> list:
    import capo_sagemaker.types.ec2_capacity_reservation

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.ec2_capacity_reservation.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> Ec2CapacityReservationsList:
    import capo_sagemaker.types.ec2_capacity_reservation

    out: Ec2CapacityReservationsList = []
    for item in data:
        out.append(
            capo_sagemaker.types.ec2_capacity_reservation.deserialize_aws_json_1_1(item)
        )
    return out
