"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#InboundFederationLambdaVersionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

InboundFederationLambdaVersionType: TypeAlias = Literal["V1_0",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("V1_0",))


def serialize_aws_json_1_1(value: InboundFederationLambdaVersionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InboundFederationLambdaVersionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown InboundFederationLambdaVersionType value: {data!r}"
        )
    return cast(InboundFederationLambdaVersionType, data)
