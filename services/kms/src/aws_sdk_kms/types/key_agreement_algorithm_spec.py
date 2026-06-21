"""Generated from Smithy shape ``com.amazonaws.kms#KeyAgreementAlgorithmSpec``."""

from typing import Literal, TypeAlias, cast

KeyAgreementAlgorithmSpec: TypeAlias = Literal["ECDH",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyAgreementAlgorithmSpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyAgreementAlgorithmSpec:
    return cast(KeyAgreementAlgorithmSpec, data)
