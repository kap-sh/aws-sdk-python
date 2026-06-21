"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#DeliveryModel``."""

from typing import Literal, TypeAlias, cast

DeliveryModel: TypeAlias = Literal[
    "SaaS or PaaS",
    "BYOL or AMI",
    "Managed Services",
    "Professional Services",
    "Resell",
    "Other",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeliveryModel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DeliveryModel:
    return cast(DeliveryModel, data)
