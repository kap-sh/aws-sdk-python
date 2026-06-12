"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationItemStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

ConfigurationItemStatus: TypeAlias = Literal[
    "OK",
    "ResourceDiscovered",
    "ResourceNotRecorded",
    "ResourceDeleted",
    "ResourceDeletedNotRecorded",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "OK",
        "ResourceDiscovered",
        "ResourceNotRecorded",
        "ResourceDeleted",
        "ResourceDeletedNotRecorded",
    )
)


def serialize_aws_json_1_1(value: ConfigurationItemStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigurationItemStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ConfigurationItemStatus value: {data!r}")
    return cast(ConfigurationItemStatus, data)
