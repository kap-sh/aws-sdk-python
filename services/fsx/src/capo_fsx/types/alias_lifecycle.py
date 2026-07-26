"""Generated from Smithy shape ``com.amazonaws.fsx#AliasLifecycle``."""

from typing import Literal, TypeAlias, cast

AliasLifecycle: TypeAlias = Literal[
    "AVAILABLE",
    "CREATING",
    "DELETING",
    "CREATE_FAILED",
    "DELETE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AliasLifecycle) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AliasLifecycle:
    return cast(AliasLifecycle, data)
