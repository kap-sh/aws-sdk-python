"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#Program``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_channel.errors import DeserializationError

Program: TypeAlias = Literal[
    "SOLUTION_PROVIDER",
    "DISTRIBUTION",
    "DISTRIBUTION_SELLER",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SOLUTION_PROVIDER",
        "DISTRIBUTION",
        "DISTRIBUTION_SELLER",
    )
)


def serialize_aws_json_1_0(value: Program) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Program:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Program value: {data!r}")
    return cast(Program, data)
