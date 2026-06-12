"""Generated from Smithy shape ``com.amazonaws.directoryservice#CertificateState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_directory_service.errors import DeserializationError

CertificateState: TypeAlias = Literal[
    "Registering",
    "Registered",
    "RegisterFailed",
    "Deregistering",
    "Deregistered",
    "DeregisterFailed",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Registering",
        "Registered",
        "RegisterFailed",
        "Deregistering",
        "Deregistered",
        "DeregisterFailed",
    )
)


def serialize_aws_json_1_1(value: CertificateState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateState value: {data!r}")
    return cast(CertificateState, data)
