"""Generated from Smithy shape ``com.amazonaws.codecommit#ObjectTypeEnum``."""

from typing import Literal, TypeAlias, cast

ObjectTypeEnum: TypeAlias = Literal[
    "FILE",
    "DIRECTORY",
    "GIT_LINK",
    "SYMBOLIC_LINK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ObjectTypeEnum:
    return cast(ObjectTypeEnum, data)
