"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#OpenIdIssuer``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_verifiedpermissions.errors import DeserializationError

OpenIdIssuer: TypeAlias = Literal["COGNITO",]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(("COGNITO",))


def serialize_aws_json_1_0(value: OpenIdIssuer) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> OpenIdIssuer:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OpenIdIssuer value: {data!r}")
    return cast(OpenIdIssuer, data)
