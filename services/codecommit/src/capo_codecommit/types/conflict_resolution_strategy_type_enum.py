"""Generated from Smithy shape ``com.amazonaws.codecommit#ConflictResolutionStrategyTypeEnum``."""

from typing import Literal, TypeAlias, cast

ConflictResolutionStrategyTypeEnum: TypeAlias = Literal[
    "NONE",
    "ACCEPT_SOURCE",
    "ACCEPT_DESTINATION",
    "AUTOMERGE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConflictResolutionStrategyTypeEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConflictResolutionStrategyTypeEnum:
    return cast(ConflictResolutionStrategyTypeEnum, data)
