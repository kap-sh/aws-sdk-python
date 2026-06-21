"""Generated from Smithy shape ``com.amazonaws.emr#OnDemandCapacityReservationUsageStrategy``."""

from typing import Literal, TypeAlias, cast

OnDemandCapacityReservationUsageStrategy: TypeAlias = Literal[
    "use-capacity-reservations-first",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OnDemandCapacityReservationUsageStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OnDemandCapacityReservationUsageStrategy:
    return cast(OnDemandCapacityReservationUsageStrategy, data)
