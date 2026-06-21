"""Generated from Smithy shape ``com.amazonaws.directoryservice#LDAPSStatus``."""

from typing import Literal, TypeAlias, cast

LDAPSStatus: TypeAlias = Literal[
    "Enabling",
    "Enabled",
    "EnableFailed",
    "Disabled",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LDAPSStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> LDAPSStatus:
    return cast(LDAPSStatus, data)
