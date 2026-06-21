"""Generated from Smithy shape ``com.amazonaws.transfer#SecurityPolicyProtocol``."""

from typing import Literal, TypeAlias, cast

SecurityPolicyProtocol: TypeAlias = Literal[
    "SFTP",
    "FTPS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecurityPolicyProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SecurityPolicyProtocol:
    return cast(SecurityPolicyProtocol, data)
