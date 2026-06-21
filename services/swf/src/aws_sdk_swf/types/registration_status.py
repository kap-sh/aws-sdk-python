"""Generated from Smithy shape ``com.amazonaws.swf#RegistrationStatus``."""

from typing import Literal, TypeAlias, cast

RegistrationStatus: TypeAlias = Literal[
    "REGISTERED",
    "DEPRECATED",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RegistrationStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RegistrationStatus:
    return cast(RegistrationStatus, data)
