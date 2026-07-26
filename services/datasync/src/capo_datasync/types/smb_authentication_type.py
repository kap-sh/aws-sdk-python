"""Generated from Smithy shape ``com.amazonaws.datasync#SmbAuthenticationType``."""

from typing import Literal, TypeAlias, cast

SmbAuthenticationType: TypeAlias = Literal[
    "NTLM",
    "KERBEROS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SmbAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SmbAuthenticationType:
    return cast(SmbAuthenticationType, data)
