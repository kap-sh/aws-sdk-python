"""Generated from Smithy shape ``com.amazonaws.apprunner#CustomDomainAssociationStatus``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_0(value: CustomDomainAssociationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CustomDomainAssociationStatus:
    return cast(CustomDomainAssociationStatus, data)
