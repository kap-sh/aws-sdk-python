"""Generated from Smithy shape ``com.amazonaws.licensemanager#ProductCodeType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

ProductCodeType: TypeAlias = Literal["marketplace",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("marketplace",))


def serialize_aws_json_1_1(value: ProductCodeType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProductCodeType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ProductCodeType value: {data!r}")
    return cast(ProductCodeType, data)
