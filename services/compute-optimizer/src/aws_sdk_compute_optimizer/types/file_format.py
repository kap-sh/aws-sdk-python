"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#FileFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_compute_optimizer.errors import DeserializationError

FileFormat: TypeAlias = Literal["Csv",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("Csv",))


def serialize_aws_json_1_0(value: FileFormat) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FileFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FileFormat value: {data!r}")
    return cast(FileFormat, data)
