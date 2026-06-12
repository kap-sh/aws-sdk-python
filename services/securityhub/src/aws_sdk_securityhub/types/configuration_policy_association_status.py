"""Generated from Smithy shape ``com.amazonaws.securityhub#ConfigurationPolicyAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

ConfigurationPolicyAssociationStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESS",
    "FAILED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "SUCCESS",
        "FAILED",
    )
)


def serialize_json(value: ConfigurationPolicyAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> ConfigurationPolicyAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ConfigurationPolicyAssociationStatus value: {data!r}"
        )
    return cast(ConfigurationPolicyAssociationStatus, data)
