"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#OpenIdIssuer``."""

from typing import Literal, TypeAlias, cast

OpenIdIssuer: TypeAlias = Literal["COGNITO",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: OpenIdIssuer) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OpenIdIssuer:
    return cast(OpenIdIssuer, data)
