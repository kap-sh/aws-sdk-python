"""Generated from Smithy shape ``com.amazonaws.sagemaker#CodeRepositorySortOrder``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

CodeRepositorySortOrder: TypeAlias = Literal[
    "Ascending",
    "Descending",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Ascending",
        "Descending",
    )
)


def serialize_aws_json_1_1(value: CodeRepositorySortOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CodeRepositorySortOrder:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CodeRepositorySortOrder value: {data!r}")
    return cast(CodeRepositorySortOrder, data)
