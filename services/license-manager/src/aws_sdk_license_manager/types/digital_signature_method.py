"""Generated from Smithy shape ``com.amazonaws.licensemanager#DigitalSignatureMethod``."""

from typing import Literal, TypeAlias, cast

DigitalSignatureMethod: TypeAlias = Literal["JWT_PS384",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DigitalSignatureMethod) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DigitalSignatureMethod:
    return cast(DigitalSignatureMethod, data)
