"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#RxNormAttributeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehendmedical.errors import DeserializationError

RxNormAttributeType: TypeAlias = Literal[
    "DOSAGE",
    "DURATION",
    "FORM",
    "FREQUENCY",
    "RATE",
    "ROUTE_OR_MODE",
    "STRENGTH",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DOSAGE",
        "DURATION",
        "FORM",
        "FREQUENCY",
        "RATE",
        "ROUTE_OR_MODE",
        "STRENGTH",
    )
)


def serialize_aws_json_1_1(value: RxNormAttributeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RxNormAttributeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RxNormAttributeType value: {data!r}")
    return cast(RxNormAttributeType, data)
