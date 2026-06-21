"""Generated from Smithy shape ``com.amazonaws.mturk#HITStatus``."""

from typing import Literal, TypeAlias, cast

HITStatus: TypeAlias = Literal[
    "Assignable",
    "Unassignable",
    "Reviewable",
    "Reviewing",
    "Disposed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HITStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HITStatus:
    return cast(HITStatus, data)
