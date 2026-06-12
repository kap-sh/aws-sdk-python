"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionConfigurationPropertyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codepipeline.errors import DeserializationError

ActionConfigurationPropertyType: TypeAlias = Literal[
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


def serialize_aws_json_1_1(value: ActionConfigurationPropertyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActionConfigurationPropertyType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ActionConfigurationPropertyType value: {data!r}"
        )
    return cast(ActionConfigurationPropertyType, data)
