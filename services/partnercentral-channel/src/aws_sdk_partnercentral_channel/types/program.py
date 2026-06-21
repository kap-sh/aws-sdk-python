"""Generated from Smithy shape ``com.amazonaws.partnercentralchannel#Program``."""

from typing import Literal, TypeAlias, cast

Program: TypeAlias = Literal[
    "SOLUTION_PROVIDER",
    "DISTRIBUTION",
    "DISTRIBUTION_SELLER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Program) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> Program:
    return cast(Program, data)
