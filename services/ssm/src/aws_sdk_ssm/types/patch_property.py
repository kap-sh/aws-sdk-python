"""Generated from Smithy shape ``com.amazonaws.ssm#PatchProperty``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

PatchProperty: TypeAlias = Literal[
    "PRODUCT",
    "PRODUCT_FAMILY",
    "CLASSIFICATION",
    "MSRC_SEVERITY",
    "PRIORITY",
    "SEVERITY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PRODUCT",
        "PRODUCT_FAMILY",
        "CLASSIFICATION",
        "MSRC_SEVERITY",
        "PRIORITY",
        "SEVERITY",
    )
)


def serialize_aws_json_1_1(value: PatchProperty) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchProperty:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PatchProperty value: {data!r}")
    return cast(PatchProperty, data)
