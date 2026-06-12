"""Generated from Smithy shape ``com.amazonaws.frauddetector#UnlabeledEventsTreatment``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_frauddetector.errors import DeserializationError

UnlabeledEventsTreatment: TypeAlias = Literal[
    "IGNORE",
    "FRAUD",
    "LEGIT",
    "AUTO",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IGNORE",
        "FRAUD",
        "LEGIT",
        "AUTO",
    )
)


def serialize_aws_json_1_1(value: UnlabeledEventsTreatment) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UnlabeledEventsTreatment:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UnlabeledEventsTreatment value: {data!r}")
    return cast(UnlabeledEventsTreatment, data)
