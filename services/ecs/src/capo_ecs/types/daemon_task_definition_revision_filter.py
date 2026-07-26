"""Generated from Smithy shape ``com.amazonaws.ecs#DaemonTaskDefinitionRevisionFilter``."""

from typing import Literal, TypeAlias, cast

DaemonTaskDefinitionRevisionFilter: TypeAlias = Literal["LAST_REGISTERED",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DaemonTaskDefinitionRevisionFilter) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DaemonTaskDefinitionRevisionFilter:
    return cast(DaemonTaskDefinitionRevisionFilter, data)
