"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CharLengthSemantics``."""

from typing import Literal, TypeAlias, cast

CharLengthSemantics: TypeAlias = Literal[
    "default",
    "char",
    "byte",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CharLengthSemantics) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CharLengthSemantics:
    return cast(CharLengthSemantics, data)
