"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#FulfillmentOptionType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: FulfillmentOptionType) -> str:
    return value


def deserialize_json(data: str) -> FulfillmentOptionType:
    return cast(FulfillmentOptionType, data)
