"""Generated from Smithy shape ``com.amazonaws.costexplorer#GroupDefinitionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

GroupDefinitionType: TypeAlias = Literal[
    "DIMENSION",
    "TAG",
    "COST_CATEGORY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DIMENSION",
        "TAG",
        "COST_CATEGORY",
    )
)


def serialize_aws_json_1_1(value: GroupDefinitionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> GroupDefinitionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GroupDefinitionType value: {data!r}")
    return cast(GroupDefinitionType, data)
