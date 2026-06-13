"""Generated from Smithy shape ``com.amazonaws.emr#OutputNotebookFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr.errors import DeserializationError

OutputNotebookFormat: TypeAlias = Literal["HTML",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("HTML",))


def serialize_aws_json_1_1(value: OutputNotebookFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OutputNotebookFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OutputNotebookFormat value: {data!r}")
    return cast(OutputNotebookFormat, data)
