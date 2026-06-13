"""Generated from Smithy shape ``com.amazonaws.mailmanager#ArchiveStringOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

ArchiveStringOperator: TypeAlias = Literal["CONTAINS",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("CONTAINS",))


def serialize_aws_json_1_0(value: ArchiveStringOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ArchiveStringOperator:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ArchiveStringOperator value: {data!r}")
    return cast(ArchiveStringOperator, data)
