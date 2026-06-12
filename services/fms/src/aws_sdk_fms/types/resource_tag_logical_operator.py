"""Generated from Smithy shape ``com.amazonaws.fms#ResourceTagLogicalOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_fms.errors import DeserializationError

ResourceTagLogicalOperator: TypeAlias = Literal[
    "AND",
    "OR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AND",
        "OR",
    )
)


def serialize_aws_json_1_1(value: ResourceTagLogicalOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceTagLogicalOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ResourceTagLogicalOperator value: {data!r}"
        )
    return cast(ResourceTagLogicalOperator, data)
