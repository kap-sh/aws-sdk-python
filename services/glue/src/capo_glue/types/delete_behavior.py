"""Generated from Smithy shape ``com.amazonaws.glue#DeleteBehavior``."""

from typing import Literal, TypeAlias, cast

DeleteBehavior: TypeAlias = Literal[
    "LOG",
    "DELETE_FROM_DATABASE",
    "DEPRECATE_IN_DATABASE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeleteBehavior:
    return cast(DeleteBehavior, data)
