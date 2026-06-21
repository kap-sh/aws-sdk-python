"""Generated from Smithy shape ``com.amazonaws.ecr#RCTAppliedFor``."""

from typing import Literal, TypeAlias, cast

RCTAppliedFor: TypeAlias = Literal[
    "REPLICATION",
    "PULL_THROUGH_CACHE",
    "CREATE_ON_PUSH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RCTAppliedFor) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RCTAppliedFor:
    return cast(RCTAppliedFor, data)
