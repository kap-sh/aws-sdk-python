"""Generated from Smithy shape ``com.amazonaws.emr#OnDemandCapacityReservationPreference``."""

from typing import Literal, TypeAlias, cast

OnDemandCapacityReservationPreference: TypeAlias = Literal[
    "open",
    "none",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnDemandCapacityReservationPreference) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OnDemandCapacityReservationPreference:
    return cast(OnDemandCapacityReservationPreference, data)
