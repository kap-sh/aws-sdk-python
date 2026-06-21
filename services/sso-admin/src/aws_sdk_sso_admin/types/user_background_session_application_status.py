"""Generated from Smithy shape ``com.amazonaws.ssoadmin#UserBackgroundSessionApplicationStatus``."""

from typing import Literal, TypeAlias, cast

UserBackgroundSessionApplicationStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserBackgroundSessionApplicationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UserBackgroundSessionApplicationStatus:
    return cast(UserBackgroundSessionApplicationStatus, data)
