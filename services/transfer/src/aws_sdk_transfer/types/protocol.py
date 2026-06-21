"""Generated from Smithy shape ``com.amazonaws.transfer#Protocol``."""

from typing import Literal, TypeAlias, cast

Protocol: TypeAlias = Literal[
    "SFTP",
    "FTP",
    "FTPS",
    "AS2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Protocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Protocol:
    return cast(Protocol, data)
