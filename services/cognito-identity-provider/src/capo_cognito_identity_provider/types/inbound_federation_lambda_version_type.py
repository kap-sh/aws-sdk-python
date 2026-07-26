"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#InboundFederationLambdaVersionType``."""

from typing import Literal, TypeAlias, cast

InboundFederationLambdaVersionType: TypeAlias = Literal["V1_0",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InboundFederationLambdaVersionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InboundFederationLambdaVersionType:
    return cast(InboundFederationLambdaVersionType, data)
