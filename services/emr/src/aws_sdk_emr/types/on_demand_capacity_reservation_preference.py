"""Generated from Smithy shape ``com.amazonaws.emr#OnDemandCapacityReservationPreference``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

OnDemandCapacityReservationPreference: TypeAlias = Literal[
    "open",
    "none",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "open",
        "none",
    )
)


def serialize_aws_json_1_1(value: OnDemandCapacityReservationPreference) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OnDemandCapacityReservationPreference:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown OnDemandCapacityReservationPreference value: {data!r}"
        )
    return cast(OnDemandCapacityReservationPreference, data)
