"""Generated from Smithy shape ``com.amazonaws.sagemaker#CapacityReservationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

CapacityReservationType: TypeAlias = Literal[
    "ODCR",
    "CRG",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ODCR",
        "CRG",
    )
)


def serialize_aws_json_1_1(value: CapacityReservationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CapacityReservationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CapacityReservationType value: {data!r}")
    return cast(CapacityReservationType, data)
