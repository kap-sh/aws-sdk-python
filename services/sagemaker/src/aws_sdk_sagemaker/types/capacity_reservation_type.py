"""Generated from Smithy shape ``com.amazonaws.sagemaker#CapacityReservationType``."""

from typing import Literal, TypeAlias, cast

CapacityReservationType: TypeAlias = Literal[
    "ODCR",
    "CRG",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityReservationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityReservationType:
    return cast(CapacityReservationType, data)
