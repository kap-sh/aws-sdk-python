"""Generated from Smithy shape ``com.amazonaws.licensemanager#ActivationOverrideBehavior``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

ActivationOverrideBehavior: TypeAlias = Literal[
    "DISTRIBUTED_GRANTS_ONLY",
    "ALL_GRANTS_PERMITTED_BY_ISSUER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISTRIBUTED_GRANTS_ONLY",
        "ALL_GRANTS_PERMITTED_BY_ISSUER",
    )
)


def serialize_aws_json_1_1(value: ActivationOverrideBehavior) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActivationOverrideBehavior:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ActivationOverrideBehavior value: {data!r}"
        )
    return cast(ActivationOverrideBehavior, data)
