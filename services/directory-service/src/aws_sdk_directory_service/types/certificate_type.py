"""Generated from Smithy shape ``com.amazonaws.directoryservice#CertificateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

CertificateType: TypeAlias = Literal[
    "ClientCertAuth",
    "ClientLDAPS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ClientCertAuth",
        "ClientLDAPS",
    )
)


def serialize_aws_json_1_1(value: CertificateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateType value: {data!r}")
    return cast(CertificateType, data)
