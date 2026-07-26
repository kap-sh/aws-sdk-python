"""Generated from Smithy shape ``com.amazonaws.lightsail#DnsRecordCreationStateCode``."""

from typing import Literal, TypeAlias, cast

DnsRecordCreationStateCode: TypeAlias = Literal[
    "SUCCEEDED",
    "STARTED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DnsRecordCreationStateCode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DnsRecordCreationStateCode:
    return cast(DnsRecordCreationStateCode, data)
