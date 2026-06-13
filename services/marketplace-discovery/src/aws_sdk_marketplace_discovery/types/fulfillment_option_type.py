"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#FulfillmentOptionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_marketplace_discovery.errors import DeserializationError

FulfillmentOptionType: TypeAlias = Literal[
    "AMAZON_MACHINE_IMAGE",
    "API",
    "CLOUDFORMATION_TEMPLATE",
    "CONTAINER",
    "HELM",
    "EKS_ADD_ON",
    "EC2_IMAGE_BUILDER_COMPONENT",
    "DATA_EXCHANGE",
    "PROFESSIONAL_SERVICES",
    "SAAS",
    "SAGEMAKER_ALGORITHM",
    "SAGEMAKER_MODEL",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AMAZON_MACHINE_IMAGE",
        "API",
        "CLOUDFORMATION_TEMPLATE",
        "CONTAINER",
        "HELM",
        "EKS_ADD_ON",
        "EC2_IMAGE_BUILDER_COMPONENT",
        "DATA_EXCHANGE",
        "PROFESSIONAL_SERVICES",
        "SAAS",
        "SAGEMAKER_ALGORITHM",
        "SAGEMAKER_MODEL",
    )
)


def serialize_json(value: FulfillmentOptionType) -> str:
    return value


def deserialize_json(data: str) -> FulfillmentOptionType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FulfillmentOptionType value: {data!r}")
    return cast(FulfillmentOptionType, data)
