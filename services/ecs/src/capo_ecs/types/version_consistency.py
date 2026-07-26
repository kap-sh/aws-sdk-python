"""Generated from Smithy shape ``com.amazonaws.ecs#VersionConsistency``."""

from typing import Literal, TypeAlias, cast

VersionConsistency: TypeAlias = Literal[
    "enabled",
    "disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: VersionConsistency) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VersionConsistency:
    return cast(VersionConsistency, data)
