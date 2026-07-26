"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#SslSecurityProtocolValue``."""

from typing import Literal, TypeAlias, cast

SslSecurityProtocolValue: TypeAlias = Literal[
    "plaintext",
    "ssl-encryption",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SslSecurityProtocolValue) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SslSecurityProtocolValue:
    return cast(SslSecurityProtocolValue, data)
