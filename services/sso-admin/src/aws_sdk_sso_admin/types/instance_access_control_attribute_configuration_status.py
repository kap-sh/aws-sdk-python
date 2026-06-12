"""Generated from Smithy shape ``com.amazonaws.ssoadmin#InstanceAccessControlAttributeConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

InstanceAccessControlAttributeConfigurationStatus: TypeAlias = Literal[
    "ENABLED",
    "CREATION_IN_PROGRESS",
    "CREATION_FAILED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "CREATION_IN_PROGRESS",
        "CREATION_FAILED",
    )
)


def serialize_aws_json_1_1(
    value: InstanceAccessControlAttributeConfigurationStatus,
) -> str:
    return value


def deserialize_aws_json_1_1(
    data: str,
) -> InstanceAccessControlAttributeConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InstanceAccessControlAttributeConfigurationStatus value: {data!r}"
        )
    return cast(InstanceAccessControlAttributeConfigurationStatus, data)
