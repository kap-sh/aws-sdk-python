"""Generated from Smithy shape ``com.amazonaws.sagemaker#VendorGuidance``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

VendorGuidance: TypeAlias = Literal[
    "NOT_PROVIDED",
    "STABLE",
    "TO_BE_ARCHIVED",
    "ARCHIVED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NOT_PROVIDED",
        "STABLE",
        "TO_BE_ARCHIVED",
        "ARCHIVED",
    )
)


def serialize_aws_json_1_1(value: VendorGuidance) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> VendorGuidance:
    if data not in _VALUES:
        raise DeserializationError(f"unknown VendorGuidance value: {data!r}")
    return cast(VendorGuidance, data)
