"""Generated from Smithy shape ``com.amazonaws.gamelift#CertificateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_gamelift.errors import DeserializationError

CertificateType: TypeAlias = Literal[
    "DISABLED",
    "GENERATED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "GENERATED",
    )
)


def serialize_aws_json_1_1(value: CertificateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateType value: {data!r}")
    return cast(CertificateType, data)
