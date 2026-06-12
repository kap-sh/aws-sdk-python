"""Generated from Smithy shape ``com.amazonaws.configservice#MaximumExecutionFrequency``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

MaximumExecutionFrequency: TypeAlias = Literal[
    "One_Hour",
    "Three_Hours",
    "Six_Hours",
    "Twelve_Hours",
    "TwentyFour_Hours",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "One_Hour",
        "Three_Hours",
        "Six_Hours",
        "Twelve_Hours",
        "TwentyFour_Hours",
    )
)


def serialize_aws_json_1_1(value: MaximumExecutionFrequency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MaximumExecutionFrequency:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MaximumExecutionFrequency value: {data!r}")
    return cast(MaximumExecutionFrequency, data)
