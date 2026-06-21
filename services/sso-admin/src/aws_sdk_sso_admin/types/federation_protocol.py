"""Generated from Smithy shape ``com.amazonaws.ssoadmin#FederationProtocol``."""

from typing import Literal, TypeAlias, cast

FederationProtocol: TypeAlias = Literal[
    "SAML",
    "OAUTH",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FederationProtocol) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FederationProtocol:
    return cast(FederationProtocol, data)
