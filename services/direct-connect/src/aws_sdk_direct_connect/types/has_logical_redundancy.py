"""Generated from Smithy shape ``com.amazonaws.directconnect#HasLogicalRedundancy``."""

from typing import Literal, TypeAlias, cast

HasLogicalRedundancy: TypeAlias = Literal[
    "unknown",
    "yes",
    "no",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HasLogicalRedundancy) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HasLogicalRedundancy:
    return cast(HasLogicalRedundancy, data)
