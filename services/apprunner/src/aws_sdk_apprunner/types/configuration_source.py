"""Generated from Smithy shape ``com.amazonaws.apprunner#ConfigurationSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

ConfigurationSource: TypeAlias = Literal[
    "REPOSITORY",
    "API",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REPOSITORY",
        "API",
    )
)


def serialize_aws_json_1_0(value: ConfigurationSource) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ConfigurationSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationSource value: {data!r}")
    return cast(ConfigurationSource, data)
