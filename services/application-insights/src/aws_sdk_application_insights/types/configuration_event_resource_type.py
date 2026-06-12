"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ConfigurationEventResourceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

ConfigurationEventResourceType: TypeAlias = Literal[
    "CLOUDWATCH_ALARM",
    "CLOUDWATCH_LOG",
    "CLOUDFORMATION",
    "SSM_ASSOCIATION",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLOUDWATCH_ALARM",
        "CLOUDWATCH_LOG",
        "CLOUDFORMATION",
        "SSM_ASSOCIATION",
    )
)


def serialize_aws_json_1_1(value: ConfigurationEventResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigurationEventResourceType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConfigurationEventResourceType value: {data!r}"
        )
    return cast(ConfigurationEventResourceType, data)
