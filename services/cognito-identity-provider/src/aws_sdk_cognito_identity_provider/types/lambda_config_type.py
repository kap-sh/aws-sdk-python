"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#LambdaConfigType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.arn_type
    import aws_sdk_cognito_identity_provider.types.custom_email_lambda_version_config_type
    import aws_sdk_cognito_identity_provider.types.custom_sms_lambda_version_config_type
    import aws_sdk_cognito_identity_provider.types.inbound_federation_lambda_type
    import aws_sdk_cognito_identity_provider.types.pre_token_generation_version_config_type


class LambdaConfigType(TypedDict):
    pre_sign_up: NotRequired["aws_sdk_cognito_identity_provider.types.arn_type.ArnType"]
    """<p>The configuration of a <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html\">pre sign-up Lambda trigger</a> in a user pool. This trigger evaluates new users and can bypass confirmation, <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html\">link a federated user profile</a>, or block sign-up requests.</p>"""
    custom_message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
    ]
    """<p>A custom message Lambda trigger. This trigger is an opportunity to customize all SMS and email messages from your user pool. When a custom message trigger is active, your user pool routes all messages to a Lambda function that returns a runtime-customized message subject and body for your user pool to deliver to a user.</p>"""
    post_confirmation: NotRequired[
        "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
    ]
    """<p>The configuration of a <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-confirmation.html\">post confirmation Lambda trigger</a> in a user pool. This trigger can take custom actions after a user confirms their user account and their email address or phone number.</p>"""
    pre_authentication: NotRequired[
        "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
    ]
    """<p>The configuration of a <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-authentication.html\">pre authentication trigger</a> in a user pool. This trigger can evaluate and modify user sign-in events.</p>"""
    post_authentication: NotRequired[
        "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
    ]
    """<p>The configuration of a <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-post-authentication.html\">post authentication Lambda trigger</a> in a user pool. This trigger can take custom actions after a user signs in.</p>"""
    define_auth_challenge: NotRequired[
        "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
    ]
    """<p>The configuration of a define auth challenge Lambda trigger, one of three triggers in the sequence of the <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html\">custom authentication challenge triggers</a>.</p>"""
    create_auth_challenge: NotRequired[
        "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
    ]
    """<p>The configuration of a create auth challenge Lambda trigger, one of three triggers in the sequence of the <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html\">custom authentication challenge triggers</a>.</p>"""
    verify_auth_challenge_response: NotRequired[
        "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
    ]
    """<p>The configuration of a verify auth challenge Lambda trigger, one of three triggers in the sequence of the <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-challenge.html\">custom authentication challenge triggers</a>.</p>"""
    pre_token_generation: NotRequired[
        "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
    ]
    """<p>The legacy configuration of a <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html\">pre token generation Lambda trigger</a> in a user pool.</p> <p>Set this parameter for legacy purposes. If you also set an ARN in <code>PreTokenGenerationConfig</code>, its value must be identical to <code>PreTokenGeneration</code>. For new instances of pre token generation triggers, set the <code>LambdaArn</code> of <code>PreTokenGenerationConfig</code>.</p>"""
    user_migration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.arn_type.ArnType"
    ]
    """<p>The configuration of a <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-migrate-user.html\">migrate user Lambda trigger</a> in a user pool. This trigger can create user profiles when users sign in or attempt to reset their password with credentials that don't exist yet.</p>"""
    pre_token_generation_config: NotRequired[
        "aws_sdk_cognito_identity_provider.types.pre_token_generation_version_config_type.PreTokenGenerationVersionConfigType"
    ]
    """<p>The detailed configuration of a <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html\">pre token generation Lambda trigger</a> in a user pool. If you also set an ARN in <code>PreTokenGeneration</code>, its value must be identical to <code>PreTokenGenerationConfig</code>.</p>"""
    custom_sms_sender: NotRequired[
        "aws_sdk_cognito_identity_provider.types.custom_sms_lambda_version_config_type.CustomSMSLambdaVersionConfigType"
    ]
    """<p>The configuration of a custom SMS sender Lambda trigger. This trigger routes all SMS notifications from a user pool to a Lambda function that delivers the message using custom logic.</p>"""
    custom_email_sender: NotRequired[
        "aws_sdk_cognito_identity_provider.types.custom_email_lambda_version_config_type.CustomEmailLambdaVersionConfigType"
    ]
    """<p>The configuration of a custom email sender Lambda trigger. This trigger routes all email notifications from a user pool to a Lambda function that delivers the message using custom logic.</p>"""
    kms_key_id: NotRequired["aws_sdk_cognito_identity_provider.types.arn_type.ArnType"]
    """<p>The ARN of an <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys\">KMS key</a>. Amazon Cognito uses the key to encrypt codes and temporary passwords sent to custom sender Lambda triggers.</p>"""
    inbound_federation: NotRequired[
        "aws_sdk_cognito_identity_provider.types.inbound_federation_lambda_type.InboundFederationLambdaType"
    ]
    """<p>The configuration of an inbound federation Lambda trigger. This trigger can transform federated user attributes during the authentication with external identity providers.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LambdaConfigType) -> dict:
    out: dict = {}
    if "pre_sign_up" in value:
        out["PreSignUp"] = value["pre_sign_up"]
    if "custom_message" in value:
        out["CustomMessage"] = value["custom_message"]
    if "post_confirmation" in value:
        out["PostConfirmation"] = value["post_confirmation"]
    if "pre_authentication" in value:
        out["PreAuthentication"] = value["pre_authentication"]
    if "post_authentication" in value:
        out["PostAuthentication"] = value["post_authentication"]
    if "define_auth_challenge" in value:
        out["DefineAuthChallenge"] = value["define_auth_challenge"]
    if "create_auth_challenge" in value:
        out["CreateAuthChallenge"] = value["create_auth_challenge"]
    if "verify_auth_challenge_response" in value:
        out["VerifyAuthChallengeResponse"] = value["verify_auth_challenge_response"]
    if "pre_token_generation" in value:
        out["PreTokenGeneration"] = value["pre_token_generation"]
    if "user_migration" in value:
        out["UserMigration"] = value["user_migration"]
    if "pre_token_generation_config" in value:
        import aws_sdk_cognito_identity_provider.types.pre_token_generation_version_config_type

        out["PreTokenGenerationConfig"] = (
            aws_sdk_cognito_identity_provider.types.pre_token_generation_version_config_type.serialize_aws_json_1_1(
                value["pre_token_generation_config"]
            )
        )
    if "custom_sms_sender" in value:
        import aws_sdk_cognito_identity_provider.types.custom_sms_lambda_version_config_type

        out["CustomSMSSender"] = (
            aws_sdk_cognito_identity_provider.types.custom_sms_lambda_version_config_type.serialize_aws_json_1_1(
                value["custom_sms_sender"]
            )
        )
    if "custom_email_sender" in value:
        import aws_sdk_cognito_identity_provider.types.custom_email_lambda_version_config_type

        out["CustomEmailSender"] = (
            aws_sdk_cognito_identity_provider.types.custom_email_lambda_version_config_type.serialize_aws_json_1_1(
                value["custom_email_sender"]
            )
        )
    if "kms_key_id" in value:
        out["KMSKeyID"] = value["kms_key_id"]
    if "inbound_federation" in value:
        import aws_sdk_cognito_identity_provider.types.inbound_federation_lambda_type

        out["InboundFederation"] = (
            aws_sdk_cognito_identity_provider.types.inbound_federation_lambda_type.serialize_aws_json_1_1(
                value["inbound_federation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> LambdaConfigType:
    out: LambdaConfigType = {}  # type: ignore[typeddict-item]
    if "PreSignUp" in data:
        out["pre_sign_up"] = data["PreSignUp"]
    if "CustomMessage" in data:
        out["custom_message"] = data["CustomMessage"]
    if "PostConfirmation" in data:
        out["post_confirmation"] = data["PostConfirmation"]
    if "PreAuthentication" in data:
        out["pre_authentication"] = data["PreAuthentication"]
    if "PostAuthentication" in data:
        out["post_authentication"] = data["PostAuthentication"]
    if "DefineAuthChallenge" in data:
        out["define_auth_challenge"] = data["DefineAuthChallenge"]
    if "CreateAuthChallenge" in data:
        out["create_auth_challenge"] = data["CreateAuthChallenge"]
    if "VerifyAuthChallengeResponse" in data:
        out["verify_auth_challenge_response"] = data["VerifyAuthChallengeResponse"]
    if "PreTokenGeneration" in data:
        out["pre_token_generation"] = data["PreTokenGeneration"]
    if "UserMigration" in data:
        out["user_migration"] = data["UserMigration"]
    if "PreTokenGenerationConfig" in data:
        import aws_sdk_cognito_identity_provider.types.pre_token_generation_version_config_type

        out["pre_token_generation_config"] = (
            aws_sdk_cognito_identity_provider.types.pre_token_generation_version_config_type.deserialize_aws_json_1_1(
                data["PreTokenGenerationConfig"]
            )
        )
    if "CustomSMSSender" in data:
        import aws_sdk_cognito_identity_provider.types.custom_sms_lambda_version_config_type

        out["custom_sms_sender"] = (
            aws_sdk_cognito_identity_provider.types.custom_sms_lambda_version_config_type.deserialize_aws_json_1_1(
                data["CustomSMSSender"]
            )
        )
    if "CustomEmailSender" in data:
        import aws_sdk_cognito_identity_provider.types.custom_email_lambda_version_config_type

        out["custom_email_sender"] = (
            aws_sdk_cognito_identity_provider.types.custom_email_lambda_version_config_type.deserialize_aws_json_1_1(
                data["CustomEmailSender"]
            )
        )
    if "KMSKeyID" in data:
        out["kms_key_id"] = data["KMSKeyID"]
    if "InboundFederation" in data:
        import aws_sdk_cognito_identity_provider.types.inbound_federation_lambda_type

        out["inbound_federation"] = (
            aws_sdk_cognito_identity_provider.types.inbound_federation_lambda_type.deserialize_aws_json_1_1(
                data["InboundFederation"]
            )
        )
    return out
