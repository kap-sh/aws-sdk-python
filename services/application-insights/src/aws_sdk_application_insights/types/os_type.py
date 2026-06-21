"""Generated from Smithy shape ``com.amazonaws.applicationinsights#OsType``."""

from typing import Literal, TypeAlias, cast

OsType: TypeAlias = Literal[
    "WINDOWS",
    "LINUX",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OsType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OsType:
    return cast(OsType, data)
