"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#AcceptType``."""

from typing import Literal, TypeAlias, cast

AcceptType: TypeAlias = Literal[
    "DELIVERED",
    "READ",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceptType:
    return cast(AcceptType, data)
