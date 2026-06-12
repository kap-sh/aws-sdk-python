"""Generated from Smithy shape ``com.amazonaws.codepipeline#RuleConfigurationPropertyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

RuleConfigurationPropertyType: TypeAlias = Literal[
    "String",
    "Number",
    "Boolean",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "String",
        "Number",
        "Boolean",
    )
)


def serialize_aws_json_1_1(value: RuleConfigurationPropertyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleConfigurationPropertyType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown RuleConfigurationPropertyType value: {data!r}"
        )
    return cast(RuleConfigurationPropertyType, data)
