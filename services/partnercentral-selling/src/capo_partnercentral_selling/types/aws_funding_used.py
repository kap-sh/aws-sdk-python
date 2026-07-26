"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsFundingUsed``."""

from typing import Literal, TypeAlias, cast

AwsFundingUsed: TypeAlias = Literal[
    "Yes",
    "No",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsFundingUsed) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AwsFundingUsed:
    return cast(AwsFundingUsed, data)
