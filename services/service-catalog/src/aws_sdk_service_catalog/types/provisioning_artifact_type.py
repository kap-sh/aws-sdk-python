"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ProvisioningArtifactType: TypeAlias = Literal[
    "CLOUD_FORMATION_TEMPLATE",
    "MARKETPLACE_AMI",
    "MARKETPLACE_CAR",
    "TERRAFORM_OPEN_SOURCE",
    "TERRAFORM_CLOUD",
    "EXTERNAL",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CLOUD_FORMATION_TEMPLATE",
        "MARKETPLACE_AMI",
        "MARKETPLACE_CAR",
        "TERRAFORM_OPEN_SOURCE",
        "TERRAFORM_CLOUD",
        "EXTERNAL",
    )
)


def serialize_aws_json_1_1(value: ProvisioningArtifactType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisioningArtifactType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProvisioningArtifactType value: {data!r}")
    return cast(ProvisioningArtifactType, data)
