"""Generated from Smithy shape ``com.amazonaws.glue#DQStopJobOnFailureTiming``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

DQStopJobOnFailureTiming: TypeAlias = Literal[
    "Immediate",
    "AfterDataLoad",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Immediate",
        "AfterDataLoad",
    )
)


def serialize_aws_json_1_1(value: DQStopJobOnFailureTiming) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DQStopJobOnFailureTiming:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DQStopJobOnFailureTiming value: {data!r}")
    return cast(DQStopJobOnFailureTiming, data)
