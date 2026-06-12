"""Generated from Smithy shape ``com.amazonaws.licensemanager#DigitalSignatureMethod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_license_manager.errors import DeserializationError

DigitalSignatureMethod: TypeAlias = Literal["JWT_PS384",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("JWT_PS384",))


def serialize_aws_json_1_1(value: DigitalSignatureMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DigitalSignatureMethod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DigitalSignatureMethod value: {data!r}")
    return cast(DigitalSignatureMethod, data)
