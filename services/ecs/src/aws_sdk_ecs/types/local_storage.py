"""Generated from Smithy shape ``com.amazonaws.ecs#LocalStorage``."""

from typing import Literal, TypeAlias, cast

LocalStorage: TypeAlias = Literal[
    "included",
    "required",
    "excluded",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocalStorage) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LocalStorage:
    return cast(LocalStorage, data)
