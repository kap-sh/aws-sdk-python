"""Generated from Smithy shape ``com.amazonaws.acm#CertificateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm.errors import DeserializationError

CertificateType: TypeAlias = Literal[
    "IMPORTED",
    "AMAZON_ISSUED",
    "PRIVATE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "IMPORTED",
        "AMAZON_ISSUED",
        "PRIVATE",
    )
)


def serialize_aws_json_1_1(value: CertificateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateType value: {data!r}")
    return cast(CertificateType, data)
