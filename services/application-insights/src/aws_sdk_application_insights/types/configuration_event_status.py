"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ConfigurationEventStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_insights.errors import DeserializationError

ConfigurationEventStatus: TypeAlias = Literal[
    "INFO",
    "WARN",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INFO",
        "WARN",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: ConfigurationEventStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigurationEventStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationEventStatus value: {data!r}")
    return cast(ConfigurationEventStatus, data)
