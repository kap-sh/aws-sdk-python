"""Generated from Smithy shape ``com.amazonaws.comprehend#DocumentClassifierMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

DocumentClassifierMode: TypeAlias = Literal[
    "MULTI_CLASS",
    "MULTI_LABEL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MULTI_CLASS",
        "MULTI_LABEL",
    )
)


def serialize_aws_json_1_1(value: DocumentClassifierMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentClassifierMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentClassifierMode value: {data!r}")
    return cast(DocumentClassifierMode, data)
