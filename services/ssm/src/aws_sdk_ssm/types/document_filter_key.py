"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentFilterKey``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

DocumentFilterKey: TypeAlias = Literal[
    "Name",
    "Owner",
    "PlatformTypes",
    "DocumentType",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Name",
        "Owner",
        "PlatformTypes",
        "DocumentType",
    )
)


def serialize_aws_json_1_1(value: DocumentFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentFilterKey:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentFilterKey value: {data!r}")
    return cast(DocumentFilterKey, data)
