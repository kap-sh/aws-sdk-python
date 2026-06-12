"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactGuidance``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_service_catalog.errors import DeserializationError

ProvisioningArtifactGuidance: TypeAlias = Literal[
    "DEFAULT",
    "DEPRECATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "DEPRECATED",
    )
)


def serialize_aws_json_1_1(value: ProvisioningArtifactGuidance) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisioningArtifactGuidance:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ProvisioningArtifactGuidance value: {data!r}"
        )
    return cast(ProvisioningArtifactGuidance, data)
