"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#DeliveryModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_partnercentral_selling.errors import DeserializationError

DeliveryModel: TypeAlias = Literal[
    "SaaS or PaaS",
    "BYOL or AMI",
    "Managed Services",
    "Professional Services",
    "Resell",
    "Other",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SaaS or PaaS",
        "BYOL or AMI",
        "Managed Services",
        "Professional Services",
        "Resell",
        "Other",
    )
)


def serialize_aws_json_1_0(value: DeliveryModel) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DeliveryModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeliveryModel value: {data!r}")
    return cast(DeliveryModel, data)
