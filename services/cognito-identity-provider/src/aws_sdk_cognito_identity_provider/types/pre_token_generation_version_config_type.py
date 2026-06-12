"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#PreTokenGenerationVersionConfigType``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.arn_type
    import aws_sdk_cognito_identity_provider.types.pre_token_generation_lambda_version_type


class PreTokenGenerationVersionConfigType(TypedDict):
    lambda_version: "aws_sdk_cognito_identity_provider.types.pre_token_generation_lambda_version_type.PreTokenGenerationLambdaVersionType"
    """<p>The user pool trigger version of the request that Amazon Cognito sends to your Lambda function. Higher-numbered versions add fields that support new features.</p>"""
    lambda_arn: "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
    """<p>The Amazon Resource Name (ARN) of the function that you want to assign to your Lambda trigger.</p> <p>This parameter and the <code>PreTokenGeneration</code> property of <code>LambdaConfig</code> have the same value. For new instances of pre token generation triggers, set <code>LambdaArn</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PreTokenGenerationVersionConfigType) -> dict:
    out: dict = {}
    import aws_sdk_cognito_identity_provider.types.pre_token_generation_lambda_version_type

    out["LambdaVersion"] = (
        aws_sdk_cognito_identity_provider.types.pre_token_generation_lambda_version_type.serialize_aws_json_1_1(
            value["lambda_version"]
        )
    )
    out["LambdaArn"] = value["lambda_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PreTokenGenerationVersionConfigType:
    out: PreTokenGenerationVersionConfigType = {}  # type: ignore[typeddict-item]
    if "LambdaVersion" in data:
        import aws_sdk_cognito_identity_provider.types.pre_token_generation_lambda_version_type

        out["lambda_version"] = (
            aws_sdk_cognito_identity_provider.types.pre_token_generation_lambda_version_type.deserialize_aws_json_1_1(
                data["LambdaVersion"]
            )
        )
    else:
        raise DeserializationError(
            "PreTokenGenerationVersionConfigType.lambda_version required"
        )
    if "LambdaArn" in data:
        out["lambda_arn"] = data["LambdaArn"]
    else:
        raise DeserializationError(
            "PreTokenGenerationVersionConfigType.lambda_arn required"
        )
    return out
