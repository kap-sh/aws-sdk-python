"""Generated from Smithy shape ``com.amazonaws.configservice#ConfigurationRecorderFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_config_service.errors import DeserializationError

ConfigurationRecorderFilterName: TypeAlias = Literal["recordingScope",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("recordingScope",))


def serialize_aws_json_1_1(value: ConfigurationRecorderFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ConfigurationRecorderFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConfigurationRecorderFilterName value: {data!r}"
        )
    return cast(ConfigurationRecorderFilterName, data)
