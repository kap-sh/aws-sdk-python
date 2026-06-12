"""Generated from Smithy shape ``com.amazonaws.sagemaker#Relation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

Relation: TypeAlias = Literal[
    "EqualTo",
    "GreaterThanOrEqualTo",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EqualTo",
        "GreaterThanOrEqualTo",
    )
)


def serialize_aws_json_1_1(value: Relation) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Relation:
    if data not in _VALUES:
        raise DeserializationError(f"unknown Relation value: {data!r}")
    return cast(Relation, data)
