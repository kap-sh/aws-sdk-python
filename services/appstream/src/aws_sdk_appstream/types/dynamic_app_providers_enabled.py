"""Generated from Smithy shape ``com.amazonaws.appstream#DynamicAppProvidersEnabled``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appstream.errors import DeserializationError

DynamicAppProvidersEnabled: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: DynamicAppProvidersEnabled) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DynamicAppProvidersEnabled:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DynamicAppProvidersEnabled value: {data!r}"
        )
    return cast(DynamicAppProvidersEnabled, data)
