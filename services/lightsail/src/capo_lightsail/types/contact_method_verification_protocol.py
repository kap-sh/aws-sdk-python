"""Generated from Smithy shape ``com.amazonaws.lightsail#ContactMethodVerificationProtocol``."""

from typing import Literal, TypeAlias, cast

ContactMethodVerificationProtocol: TypeAlias = Literal["Email",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ContactMethodVerificationProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ContactMethodVerificationProtocol:
    return cast(ContactMethodVerificationProtocol, data)
