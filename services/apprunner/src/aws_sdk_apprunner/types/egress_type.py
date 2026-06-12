"""Generated from Smithy shape ``com.amazonaws.apprunner#EgressType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

EgressType: TypeAlias = Literal[
    "DEFAULT",
    "VPC",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "VPC",
    )
)


def serialize_aws_json_1_0(value: EgressType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EgressType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EgressType value: {data!r}")
    return cast(EgressType, data)
