"""Generated from Smithy shape ``com.amazonaws.sagemaker#VariantStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

VariantStatus: TypeAlias = Literal[
    "Creating",
    "Updating",
    "Deleting",
    "ActivatingTraffic",
    "Baking",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Updating",
        "Deleting",
        "ActivatingTraffic",
        "Baking",
    )
)


def serialize_aws_json_1_1(value: VariantStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VariantStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VariantStatus value: {data!r}")
    return cast(VariantStatus, data)
