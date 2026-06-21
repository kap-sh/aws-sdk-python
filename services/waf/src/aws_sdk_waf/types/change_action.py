"""Generated from Smithy shape ``com.amazonaws.waf#ChangeAction``."""

from typing import Literal, TypeAlias, cast

ChangeAction: TypeAlias = Literal[
    "INSERT",
    "DELETE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ChangeAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ChangeAction:
    return cast(ChangeAction, data)
