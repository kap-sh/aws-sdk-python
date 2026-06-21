"""Generated from Smithy shape ``com.amazonaws.lightsail#ContactProtocol``."""

from typing import Literal, TypeAlias, cast

ContactProtocol: TypeAlias = Literal[
    "Email",
    "SMS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContactProtocol:
    return cast(ContactProtocol, data)
