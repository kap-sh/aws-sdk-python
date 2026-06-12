"""Generated from Smithy shape ``com.amazonaws.lightsail#CertificateProvider``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_lightsail.errors import DeserializationError

CertificateProvider: TypeAlias = Literal["LetsEncrypt",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("LetsEncrypt",))


def serialize_aws_json_1_1(value: CertificateProvider) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateProvider:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateProvider value: {data!r}")
    return cast(CertificateProvider, data)
