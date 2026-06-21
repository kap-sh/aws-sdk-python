"""Generated from Smithy shape ``com.amazonaws.bcmdashboards#GroupDefinitionType``."""

from typing import Literal, TypeAlias, cast

GroupDefinitionType: TypeAlias = Literal[
    "DIMENSION",
    "TAG",
    "COST_CATEGORY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GroupDefinitionType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GroupDefinitionType:
    return cast(GroupDefinitionType, data)
