"""Generated from Smithy shape ``com.amazonaws.glue#ConfigurationSource``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_glue.errors import DeserializationError

ConfigurationSource: TypeAlias = Literal[
    "catalog",
    "table",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "catalog",
        "table",
    )
)


def serialize_aws_json_1_1(value: ConfigurationSource) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigurationSource:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationSource value: {data!r}")
    return cast(ConfigurationSource, data)
