"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactPropertyName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ProvisioningArtifactPropertyName: TypeAlias = Literal["Id",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("Id",))


def serialize_aws_json_1_1(value: ProvisioningArtifactPropertyName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisioningArtifactPropertyName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProvisioningArtifactPropertyName value: {data!r}"
        )
    return cast(ProvisioningArtifactPropertyName, data)
