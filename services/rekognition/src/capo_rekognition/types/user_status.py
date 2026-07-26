"""Generated from Smithy shape ``com.amazonaws.rekognition#UserStatus``."""

from typing import Literal, TypeAlias, cast

UserStatus: TypeAlias = Literal[
    "ACTIVE",
    "UPDATING",
    "CREATING",
    "CREATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserStatus:
    return cast(UserStatus, data)
