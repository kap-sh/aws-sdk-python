"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#PreTokenGenerationLambdaVersionType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cognito_identity_provider.errors import DeserializationError

PreTokenGenerationLambdaVersionType: TypeAlias = Literal[
    "V1_0",
    "V2_0",
    "V3_0",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "V1_0",
        "V2_0",
        "V3_0",
    )
)


def serialize_aws_json_1_1(value: PreTokenGenerationLambdaVersionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreTokenGenerationLambdaVersionType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown PreTokenGenerationLambdaVersionType value: {data!r}"
        )
    return cast(PreTokenGenerationLambdaVersionType, data)
