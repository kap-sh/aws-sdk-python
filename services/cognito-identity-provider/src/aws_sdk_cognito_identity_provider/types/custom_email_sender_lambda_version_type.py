"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CustomEmailSenderLambdaVersionType``."""

from typing import Literal, TypeAlias, cast

CustomEmailSenderLambdaVersionType: TypeAlias = Literal["V1_0",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomEmailSenderLambdaVersionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomEmailSenderLambdaVersionType:
    return cast(CustomEmailSenderLambdaVersionType, data)
