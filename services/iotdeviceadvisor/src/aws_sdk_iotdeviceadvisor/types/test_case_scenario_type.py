"""Generated from Smithy shape ``com.amazonaws.iotdeviceadvisor#TestCaseScenarioType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotdeviceadvisor.errors import DeserializationError

TestCaseScenarioType: TypeAlias = Literal[
    "Advanced",
    "Basic",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Advanced",
        "Basic",
    )
)


def serialize_json(value: TestCaseScenarioType) -> str:
    return value


def deserialize_json(data: str) -> TestCaseScenarioType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TestCaseScenarioType value: {data!r}")
    return cast(TestCaseScenarioType, data)
