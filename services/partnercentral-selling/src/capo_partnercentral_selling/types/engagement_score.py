"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementScore``."""

from typing import Literal, TypeAlias, cast

EngagementScore: TypeAlias = Literal[
    "High",
    "Medium",
    "Low",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementScore) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EngagementScore:
    return cast(EngagementScore, data)
