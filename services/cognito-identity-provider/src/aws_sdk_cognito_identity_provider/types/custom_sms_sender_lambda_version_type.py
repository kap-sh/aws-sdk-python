"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CustomSMSSenderLambdaVersionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

CustomSMSSenderLambdaVersionType: TypeAlias = Literal["V1_0",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("V1_0",))


def serialize_aws_json_1_1(value: CustomSMSSenderLambdaVersionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomSMSSenderLambdaVersionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CustomSMSSenderLambdaVersionType value: {data!r}"
        )
    return cast(CustomSMSSenderLambdaVersionType, data)
