"""Generated from Smithy shape ``com.amazonaws.textract#SelectionStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_textract.errors import DeserializationError

SelectionStatus: TypeAlias = Literal[
    "SELECTED",
    "NOT_SELECTED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SELECTED",
        "NOT_SELECTED",
    )
)


def serialize_aws_json_1_1(value: SelectionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SelectionStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SelectionStatus value: {data!r}")
    return cast(SelectionStatus, data)
