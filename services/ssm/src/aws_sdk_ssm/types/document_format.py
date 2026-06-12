"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentFormat``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

DocumentFormat: TypeAlias = Literal[
    "YAML",
    "JSON",
    "TEXT",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "YAML",
        "JSON",
        "TEXT",
    )
)


def serialize_aws_json_1_1(value: DocumentFormat) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentFormat:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentFormat value: {data!r}")
    return cast(DocumentFormat, data)
