"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CustomSMSSenderLambdaVersionType``."""

from typing import Literal, TypeAlias, cast

CustomSMSSenderLambdaVersionType: TypeAlias = Literal["V1_0",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomSMSSenderLambdaVersionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomSMSSenderLambdaVersionType:
    return cast(CustomSMSSenderLambdaVersionType, data)
