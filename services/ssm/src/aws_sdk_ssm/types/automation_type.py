"""Generated from Smithy shape ``com.amazonaws.ssm#AutomationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

AutomationType: TypeAlias = Literal[
    "CrossAccount",
    "Local",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CrossAccount",
        "Local",
    )
)


def serialize_aws_json_1_1(value: AutomationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AutomationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutomationType value: {data!r}")
    return cast(AutomationType, data)
