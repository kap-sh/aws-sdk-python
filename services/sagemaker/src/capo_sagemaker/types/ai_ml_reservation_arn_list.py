"""Generated from Smithy shape ``com.amazonaws.sagemaker#AIMlReservationArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.ai_ml_reservation_arn

AIMlReservationArnList: TypeAlias = list[
    "capo_sagemaker.types.ai_ml_reservation_arn.AIMlReservationArn"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AIMlReservationArnList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> AIMlReservationArnList:
    return list(data)
