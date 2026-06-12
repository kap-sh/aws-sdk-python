"""Generated from Smithy shape ``com.amazonaws.snowball#JobState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_snowball.errors import DeserializationError

JobState: TypeAlias = Literal[
    "New",
    "PreparingAppliance",
    "PreparingShipment",
    "InTransitToCustomer",
    "WithCustomer",
    "InTransitToAWS",
    "WithAWSSortingFacility",
    "WithAWS",
    "InProgress",
    "Complete",
    "Cancelled",
    "Listing",
    "Pending",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "New",
        "PreparingAppliance",
        "PreparingShipment",
        "InTransitToCustomer",
        "WithCustomer",
        "InTransitToAWS",
        "WithAWSSortingFacility",
        "WithAWS",
        "InProgress",
        "Complete",
        "Cancelled",
        "Listing",
        "Pending",
    )
)


def serialize_aws_json_1_1(value: JobState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> JobState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown JobState value: {data!r}")
    return cast(JobState, data)
