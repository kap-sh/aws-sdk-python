"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryTriggerEventEnum``."""

from typing import Literal, TypeAlias, cast

RepositoryTriggerEventEnum: TypeAlias = Literal[
    "all",
    "updateReference",
    "createReference",
    "deleteReference",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryTriggerEventEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RepositoryTriggerEventEnum:
    return cast(RepositoryTriggerEventEnum, data)
