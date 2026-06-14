"""Generated from Smithy shape ``com.amazonaws.workspaces#CertificateBasedAuthStatusEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

CertificateBasedAuthStatusEnum: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DISABLED",
        "ENABLED",
    )
)


def serialize_aws_json_1_1(value: CertificateBasedAuthStatusEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateBasedAuthStatusEnum:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CertificateBasedAuthStatusEnum value: {data!r}"
        )
    return cast(CertificateBasedAuthStatusEnum, data)
