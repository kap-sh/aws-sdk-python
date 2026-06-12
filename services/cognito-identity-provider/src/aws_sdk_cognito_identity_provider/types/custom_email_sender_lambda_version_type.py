"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CustomEmailSenderLambdaVersionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

CustomEmailSenderLambdaVersionType: TypeAlias = Literal["V1_0",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("V1_0",))


def serialize_aws_json_1_1(value: CustomEmailSenderLambdaVersionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomEmailSenderLambdaVersionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomEmailSenderLambdaVersionType value: {data!r}"
        )
    return cast(CustomEmailSenderLambdaVersionType, data)
