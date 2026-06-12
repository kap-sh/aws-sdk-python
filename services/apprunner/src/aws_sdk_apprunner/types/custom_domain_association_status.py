"""Generated from Smithy shape ``com.amazonaws.apprunner#CustomDomainAssociationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_apprunner.errors import DeserializationError

CustomDomainAssociationStatus: TypeAlias = Literal[
    "CREATING",
    "CREATE_FAILED",
    "ACTIVE",
    "DELETING",
    "DELETE_FAILED",
    "PENDING_CERTIFICATE_DNS_VALIDATION",
    "BINDING_CERTIFICATE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "CREATE_FAILED",
        "ACTIVE",
        "DELETING",
        "DELETE_FAILED",
        "PENDING_CERTIFICATE_DNS_VALIDATION",
        "BINDING_CERTIFICATE",
    )
)


def serialize_aws_json_1_0(value: CustomDomainAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CustomDomainAssociationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomDomainAssociationStatus value: {data!r}"
        )
    return cast(CustomDomainAssociationStatus, data)
