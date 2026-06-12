"""Generated from Smithy shape ``com.amazonaws.kendra#AdditionalResultAttributeValueType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

AdditionalResultAttributeValueType: TypeAlias = Literal["TEXT_WITH_HIGHLIGHTS_VALUE",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("TEXT_WITH_HIGHLIGHTS_VALUE",))


def serialize_aws_json_1_1(value: AdditionalResultAttributeValueType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdditionalResultAttributeValueType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown AdditionalResultAttributeValueType value: {data!r}"
        )
    return cast(AdditionalResultAttributeValueType, data)
