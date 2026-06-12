"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookOutputOption``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

NotebookOutputOption: TypeAlias = Literal[
    "Allowed",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Allowed",
        "Disabled",
    )
)


def serialize_aws_json_1_1(value: NotebookOutputOption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookOutputOption:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotebookOutputOption value: {data!r}")
    return cast(NotebookOutputOption, data)
