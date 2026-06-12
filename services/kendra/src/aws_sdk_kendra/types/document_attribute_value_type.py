"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentAttributeValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

DocumentAttributeValueType: TypeAlias = Literal[
    "STRING_VALUE",
    "STRING_LIST_VALUE",
    "LONG_VALUE",
    "DATE_VALUE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING_VALUE",
        "STRING_LIST_VALUE",
        "LONG_VALUE",
        "DATE_VALUE",
    )
)


def serialize_aws_json_1_1(value: DocumentAttributeValueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentAttributeValueType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DocumentAttributeValueType value: {data!r}"
        )
    return cast(DocumentAttributeValueType, data)
