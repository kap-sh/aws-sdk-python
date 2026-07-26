"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementContextType``."""

from typing import Literal, TypeAlias, cast

EngagementContextType: TypeAlias = Literal[
    "CustomerProject",
    "Lead",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementContextType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EngagementContextType:
    return cast(EngagementContextType, data)
