"""Generated from Smithy shape ``com.amazonaws.athena#NotebookType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_athena.errors import DeserializationError

NotebookType: TypeAlias = Literal["IPYNB",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("IPYNB",))


def serialize_aws_json_1_1(value: NotebookType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotebookType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotebookType value: {data!r}")
    return cast(NotebookType, data)
