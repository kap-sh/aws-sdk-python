"""Generated from Smithy shape ``com.amazonaws.ssm#SourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

SourceType: TypeAlias = Literal[
    "AWS::EC2::Instance",
    "AWS::IoT::Thing",
    "AWS::SSM::ManagedInstance",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AWS::EC2::Instance",
        "AWS::IoT::Thing",
        "AWS::SSM::ManagedInstance",
    )
)


def serialize_aws_json_1_1(value: SourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SourceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SourceType value: {data!r}")
    return cast(SourceType, data)
