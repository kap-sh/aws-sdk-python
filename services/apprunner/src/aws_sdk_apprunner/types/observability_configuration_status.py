"""Generated from Smithy shape ``com.amazonaws.apprunner#ObservabilityConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

ObservabilityConfigurationStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_aws_json_1_0(value: ObservabilityConfigurationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ObservabilityConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ObservabilityConfigurationStatus value: {data!r}"
        )
    return cast(ObservabilityConfigurationStatus, data)
