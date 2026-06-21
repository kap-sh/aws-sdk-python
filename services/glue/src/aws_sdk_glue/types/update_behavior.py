"""Generated from Smithy shape ``com.amazonaws.glue#UpdateBehavior``."""

from typing import Literal, TypeAlias, cast

UpdateBehavior: TypeAlias = Literal[
    "LOG",
    "UPDATE_IN_DATABASE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> UpdateBehavior:
    return cast(UpdateBehavior, data)
