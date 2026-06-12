"""Generated from Smithy shape ``com.amazonaws.ssm#Fault``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

Fault: TypeAlias = Literal[
    "Client",
    "Server",
    "Unknown",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Client",
        "Server",
        "Unknown",
    )
)


def serialize_aws_json_1_1(value: Fault) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Fault:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Fault value: {data!r}")
    return cast(Fault, data)
