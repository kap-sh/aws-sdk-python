"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.integer
    import aws_sdk_securityhub.types.non_empty_string


class AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails(TypedDict, closed=True):
    authorizer_result_ttl_in_seconds: NotRequired[
        "aws_sdk_securityhub.types.integer.Integer"
    ]
    """<p> The number of seconds a response should be cached for. The default is 5 minutes (300 seconds). </p>"""
    authorizer_uri: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> The Amazon Resource Name (ARN) of the Lambda function to be called for authorization. This can be a standard Lambda ARN, a version ARN (.../v3), or an alias ARN. </p>"""
    identity_validation_expression: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p> A regular expression for validation of tokens before the Lambda function is called. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails) -> dict:
    out: dict = {}
    if "authorizer_result_ttl_in_seconds" in value:
        out["AuthorizerResultTtlInSeconds"] = value["authorizer_result_ttl_in_seconds"]
    if "authorizer_uri" in value:
        out["AuthorizerUri"] = value["authorizer_uri"]
    if "identity_validation_expression" in value:
        out["IdentityValidationExpression"] = value["identity_validation_expression"]
    return out


def deserialize_json(data: dict) -> AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails:
    out: AwsAppSyncGraphQlApiLambdaAuthorizerConfigDetails = {}  # type: ignore[typeddict-item]
    if "AuthorizerResultTtlInSeconds" in data:
        out["authorizer_result_ttl_in_seconds"] = data["AuthorizerResultTtlInSeconds"]
    if "AuthorizerUri" in data:
        out["authorizer_uri"] = data["AuthorizerUri"]
    if "IdentityValidationExpression" in data:
        out["identity_validation_expression"] = data["IdentityValidationExpression"]
    return out
