"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#SmsConfigurationType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cognito_identity_provider.types.arn_type
    import capo_cognito_identity_provider.types.region_code_type
    import capo_cognito_identity_provider.types.string_type


class SmsConfigurationType(TypedDict, closed=True):
    sns_caller_arn: "capo_cognito_identity_provider.types.arn_type.ArnType"
    r"""<p>The Amazon Resource Name (ARN) of the Amazon SNS caller. This is the ARN of the IAM role in your Amazon Web Services account that Amazon Cognito will use to send SMS messages. SMS messages are subject to a <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html\">spending limit</a>. </p>"""
    external_id: NotRequired[
        "capo_cognito_identity_provider.types.string_type.StringType"
    ]
    r"""<p>The external ID provides additional security for your IAM role. You can use an <code>ExternalId</code> with the IAM role that you use with Amazon SNS to send SMS messages for your user pool. If you provide an <code>ExternalId</code>, your Amazon Cognito user pool includes it in the request to assume your IAM role. You can configure the role trust policy to require that Amazon Cognito, and any principal, provide the <code>ExternalID</code>. If you use the Amazon Cognito Management Console to create a role for SMS multi-factor authentication (MFA), Amazon Cognito creates a role with the required permissions and a trust policy that demonstrates use of the <code>ExternalId</code>.</p> <p>For more information about the <code>ExternalId</code> of a role, see <a href=\"https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html\">How to use an external ID when granting access to your Amazon Web Services resources to a third party</a>.</p>"""
    sns_region: NotRequired[
        "capo_cognito_identity_provider.types.region_code_type.RegionCodeType"
    ]
    r"""<p>The Amazon Web Services Region to use with Amazon SNS integration. You can choose the same Region as your user pool, or a supported <b>Legacy Amazon SNS alternate Region</b>. </p> <p> Amazon Cognito resources in the Asia Pacific (Seoul) Amazon Web Services Region must use your Amazon SNS configuration in the Asia Pacific (Tokyo) Region. For more information, see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\">SMS message settings for Amazon Cognito user pools</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SmsConfigurationType) -> dict:
    out: dict = {}
    out["SnsCallerArn"] = value["sns_caller_arn"]
    if "external_id" in value:
        out["ExternalId"] = value["external_id"]
    if "sns_region" in value:
        out["SnsRegion"] = value["sns_region"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SmsConfigurationType:
    out: SmsConfigurationType = {}  # type: ignore[typeddict-item]
    if "SnsCallerArn" in data:
        out["sns_caller_arn"] = data["SnsCallerArn"]
    else:
        raise DeserializationError("SmsConfigurationType.sns_caller_arn required")
    if "ExternalId" in data:
        out["external_id"] = data["ExternalId"]
    if "SnsRegion" in data:
        out["sns_region"] = data["SnsRegion"]
    return out
