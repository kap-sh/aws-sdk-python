"""Generated from Smithy shape ``com.amazonaws.emr#OnDemandCapacityReservationUsageStrategy``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

OnDemandCapacityReservationUsageStrategy: TypeAlias = Literal[
    "use-capacity-reservations-first",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("use-capacity-reservations-first",))


def serialize_aws_json_1_1(value: OnDemandCapacityReservationUsageStrategy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OnDemandCapacityReservationUsageStrategy:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OnDemandCapacityReservationUsageStrategy value: {data!r}"
        )
    return cast(OnDemandCapacityReservationUsageStrategy, data)
