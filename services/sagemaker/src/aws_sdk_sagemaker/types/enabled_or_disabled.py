"""Generated from Smithy shape ``com.amazonaws.sagemaker#EnabledOrDisabled``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

EnabledOrDisabled: TypeAlias = Literal[
    "Enabled",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Enabled",
        "Disabled",
    )
)


def serialize_aws_json_1_1(value: EnabledOrDisabled) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EnabledOrDisabled:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EnabledOrDisabled value: {data!r}")
    return cast(EnabledOrDisabled, data)
