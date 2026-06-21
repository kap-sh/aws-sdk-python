"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#PreTokenGenerationLambdaVersionType``."""

from typing import Literal, TypeAlias, cast

PreTokenGenerationLambdaVersionType: TypeAlias = Literal[
    "V1_0",
    "V2_0",
    "V3_0",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreTokenGenerationLambdaVersionType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PreTokenGenerationLambdaVersionType:
    return cast(PreTokenGenerationLambdaVersionType, data)
