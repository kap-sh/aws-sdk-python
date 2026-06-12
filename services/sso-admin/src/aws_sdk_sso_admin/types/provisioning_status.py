"""Generated from Smithy shape ``com.amazonaws.ssoadmin#ProvisioningStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sso_admin.errors import DeserializationError

ProvisioningStatus: TypeAlias = Literal[
    "LATEST_PERMISSION_SET_PROVISIONED",
    "LATEST_PERMISSION_SET_NOT_PROVISIONED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "LATEST_PERMISSION_SET_PROVISIONED",
        "LATEST_PERMISSION_SET_NOT_PROVISIONED",
    )
)


def serialize_aws_json_1_1(value: ProvisioningStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisioningStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProvisioningStatus value: {data!r}")
    return cast(ProvisioningStatus, data)
