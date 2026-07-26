"""Generated from Smithy shape ``com.amazonaws.directoryservice#CertificateState``."""

from typing import Literal, TypeAlias, cast

CertificateState: TypeAlias = Literal[
    "Registering",
    "Registered",
    "RegisterFailed",
    "Deregistering",
    "Deregistered",
    "DeregisterFailed",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateState:
    return cast(CertificateState, data)
