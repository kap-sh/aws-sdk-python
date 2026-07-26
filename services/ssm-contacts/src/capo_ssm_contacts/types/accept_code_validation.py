"""Generated from Smithy shape ``com.amazonaws.ssmcontacts#AcceptCodeValidation``."""

from typing import Literal, TypeAlias, cast

AcceptCodeValidation: TypeAlias = Literal[
    "IGNORE",
    "ENFORCE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AcceptCodeValidation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AcceptCodeValidation:
    return cast(AcceptCodeValidation, data)
