"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#CreateUserPoolRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cognito_identity_provider.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cognito_identity_provider.types.account_recovery_setting_type
    import aws_sdk_cognito_identity_provider.types.admin_create_user_config_type
    import aws_sdk_cognito_identity_provider.types.alias_attributes_list_type
    import aws_sdk_cognito_identity_provider.types.deletion_protection_type
    import aws_sdk_cognito_identity_provider.types.device_configuration_type
    import aws_sdk_cognito_identity_provider.types.email_configuration_type
    import aws_sdk_cognito_identity_provider.types.email_verification_message_type
    import aws_sdk_cognito_identity_provider.types.email_verification_subject_type
    import aws_sdk_cognito_identity_provider.types.issuer_configuration_type
    import aws_sdk_cognito_identity_provider.types.key_configuration_type
    import aws_sdk_cognito_identity_provider.types.lambda_config_type
    import aws_sdk_cognito_identity_provider.types.schema_attributes_list_type
    import aws_sdk_cognito_identity_provider.types.sms_configuration_type
    import aws_sdk_cognito_identity_provider.types.sms_verification_message_type
    import aws_sdk_cognito_identity_provider.types.user_attribute_update_settings_type
    import aws_sdk_cognito_identity_provider.types.user_pool_add_ons_type
    import aws_sdk_cognito_identity_provider.types.user_pool_mfa_type
    import aws_sdk_cognito_identity_provider.types.user_pool_name_type
    import aws_sdk_cognito_identity_provider.types.user_pool_policy_type
    import aws_sdk_cognito_identity_provider.types.user_pool_tags_type
    import aws_sdk_cognito_identity_provider.types.user_pool_tier_type
    import aws_sdk_cognito_identity_provider.types.username_attributes_list_type
    import aws_sdk_cognito_identity_provider.types.username_configuration_type
    import aws_sdk_cognito_identity_provider.types.verification_message_template_type
    import aws_sdk_cognito_identity_provider.types.verified_attributes_list_type


class CreateUserPoolRequest(TypedDict):
    pool_name: (
        "aws_sdk_cognito_identity_provider.types.user_pool_name_type.UserPoolNameType"
    )
    """<p>A friendly name for your user pool.</p>"""
    policies: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_pool_policy_type.UserPoolPolicyType"
    ]
    r"""<p>The password policy and sign-in policy in the user pool. The password policy sets options like password complexity requirements and password history. The sign-in policy sets the options available to applications in <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/authentication-flows-selection-sdk.html#authentication-flows-selection-choice\">choice-based authentication</a>.</p>"""
    deletion_protection: NotRequired[
        "aws_sdk_cognito_identity_provider.types.deletion_protection_type.DeletionProtectionType"
    ]
    """<p>When active, <code>DeletionProtection</code> prevents accidental deletion of your user pool. Before you can delete a user pool that you have protected against deletion, you must deactivate this feature.</p> <p>When you try to delete a protected user pool in a <code>DeleteUserPool</code> API request, Amazon Cognito returns an <code>InvalidParameterException</code> error. To delete a protected user pool, send a new <code>DeleteUserPool</code> request after you deactivate deletion protection in an <code>UpdateUserPool</code> API request.</p>"""
    lambda_config: NotRequired[
        "aws_sdk_cognito_identity_provider.types.lambda_config_type.LambdaConfigType"
    ]
    """<p>A collection of user pool Lambda triggers. Amazon Cognito invokes triggers at several possible stages of authentication operations. Triggers can modify the outcome of the operations that invoked them.</p>"""
    auto_verified_attributes: NotRequired[
        "aws_sdk_cognito_identity_provider.types.verified_attributes_list_type.VerifiedAttributesListType"
    ]
    r"""<p>The attributes that you want your user pool to automatically verify. For more information, see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/signing-up-users-in-your-app.html#allowing-users-to-sign-up-and-confirm-themselves\">Verifying contact information at sign-up</a>.</p>"""
    alias_attributes: NotRequired[
        "aws_sdk_cognito_identity_provider.types.alias_attributes_list_type.AliasAttributesListType"
    ]
    r"""<p>Attributes supported as an alias for this user pool. For more information about alias attributes, see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#user-pool-settings-aliases\">Customizing sign-in attributes</a>.</p>"""
    username_attributes: NotRequired[
        "aws_sdk_cognito_identity_provider.types.username_attributes_list_type.UsernameAttributesListType"
    ]
    r"""<p>Specifies whether a user can use an email address or phone number as a username when they sign up. For more information, see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html#user-pool-settings-aliases\">Customizing sign-in attributes</a>.</p>"""
    sms_verification_message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.sms_verification_message_type.SmsVerificationMessageType"
    ]
    """<p>This parameter is no longer used.</p>"""
    email_verification_message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.email_verification_message_type.EmailVerificationMessageType"
    ]
    """<p>This parameter is no longer used.</p>"""
    email_verification_subject: NotRequired[
        "aws_sdk_cognito_identity_provider.types.email_verification_subject_type.EmailVerificationSubjectType"
    ]
    """<p>This parameter is no longer used.</p>"""
    verification_message_template: NotRequired[
        "aws_sdk_cognito_identity_provider.types.verification_message_template_type.VerificationMessageTemplateType"
    ]
    """<p>The template for the verification message that your user pool delivers to users who set an email address or phone number attribute.</p> <p>Set the email message type that corresponds to your <code>DefaultEmailOption</code> selection. For <code>CONFIRM_WITH_LINK</code>, specify an <code>EmailMessageByLink</code> and leave <code>EmailMessage</code> blank. For <code>CONFIRM_WITH_CODE</code>, specify an <code>EmailMessage</code> and leave <code>EmailMessageByLink</code> blank. When you supply both parameters with either choice, Amazon Cognito returns an error.</p>"""
    sms_authentication_message: NotRequired[
        "aws_sdk_cognito_identity_provider.types.sms_verification_message_type.SmsVerificationMessageType"
    ]
    """<p>The contents of the SMS message that your user pool sends to users in SMS OTP and MFA authentication.</p>"""
    mfa_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_pool_mfa_type.UserPoolMfaType"
    ]
    """<p>Sets multi-factor authentication (MFA) to be on, off, or optional. When <code>ON</code>, all users must set up MFA before they can sign in. When <code>OPTIONAL</code>, your application must make a client-side determination of whether a user wants to register an MFA device. For user pools with adaptive authentication with threat protection, choose <code>OPTIONAL</code>.</p> <p>When <code>MfaConfiguration</code> is <code>OPTIONAL</code>, managed login doesn't automatically prompt users to set up MFA. Amazon Cognito generates MFA prompts in API responses and in managed login for users who have chosen and configured a preferred MFA factor.</p>"""
    user_attribute_update_settings: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_attribute_update_settings_type.UserAttributeUpdateSettingsType"
    ]
    r"""<p>The settings for updates to user attributes. These settings include the property <code>AttributesRequireVerificationBeforeUpdate</code>, a user-pool setting that tells Amazon Cognito how to handle changes to the value of your users' email address and phone number attributes. For more information, see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-email-phone-verification.html#user-pool-settings-verifications-verify-attribute-updates\"> Verifying updates to email addresses and phone numbers</a>.</p>"""
    device_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.device_configuration_type.DeviceConfigurationType"
    ]
    r"""<p>The device-remembering configuration for a user pool. Device remembering or device tracking is a \"Remember me on this device\" option for user pools that perform authentication with the device key of a trusted device in the back end, instead of a user-provided MFA code. For more information about device authentication, see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html\">Working with user devices in your user pool</a>. A null value indicates that you have deactivated device remembering in your user pool.</p> <note> <p>When you provide a value for any <code>DeviceConfiguration</code> field, you activate the Amazon Cognito device-remembering feature. For more information, see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-device-tracking.html\">Working with devices</a>.</p> </note>"""
    email_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.email_configuration_type.EmailConfigurationType"
    ]
    """<p>The email configuration of your user pool. The email configuration type sets your preferred sending method, Amazon Web Services Region, and sender for messages from your user pool.</p>"""
    sms_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.sms_configuration_type.SmsConfigurationType"
    ]
    r"""<p>The settings for your Amazon Cognito user pool to send SMS messages with Amazon Simple Notification Service. To send SMS messages with Amazon SNS in the Amazon Web Services Region that you want, the Amazon Cognito user pool uses an Identity and Access Management (IAM) role in your Amazon Web Services account. For more information see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-sms-settings.html\">SMS message settings</a>.</p>"""
    user_pool_tags: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_pool_tags_type.UserPoolTagsType"
    ]
    """<p>The tag keys and values to assign to the user pool. A tag is a label that you can use to categorize and manage user pools in different ways, such as by purpose, owner, environment, or other criteria.</p>"""
    admin_create_user_config: NotRequired[
        "aws_sdk_cognito_identity_provider.types.admin_create_user_config_type.AdminCreateUserConfigType"
    ]
    """<p>The configuration for administrative creation of users. Includes the template for the invitation message for new users, the duration of temporary passwords, and permitting self-service sign-up.</p>"""
    schema: NotRequired[
        "aws_sdk_cognito_identity_provider.types.schema_attributes_list_type.SchemaAttributesListType"
    ]
    r"""<p>An array of attributes for the new user pool. You can add custom attributes and modify the properties of default attributes. The specifications in this parameter set the required attributes in your user pool. For more information, see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-attributes.html\">Working with user attributes</a>.</p>"""
    user_pool_add_ons: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_pool_add_ons_type.UserPoolAddOnsType"
    ]
    r"""<p>Contains settings for activation of threat protection, including the operating mode and additional authentication types. To log user security information but take no action, set to <code>AUDIT</code>. To configure automatic security responses to potentially unwanted traffic to your user pool, set to <code>ENFORCED</code>.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html\">Adding advanced security to a user pool</a>. To activate this setting, your user pool must be on the <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/feature-plans-features-plus.html\"> Plus tier</a>.</p>"""
    username_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.username_configuration_type.UsernameConfigurationType"
    ]
    """<p>Sets the case sensitivity option for sign-in usernames. When <code>CaseSensitive</code> is <code>false</code> (case insensitive), users can sign in with any combination of capital and lowercase letters. For example, <code>username</code>, <code>USERNAME</code>, or <code>UserName</code>, or for email, <code>email@example.com</code> or <code>EMaiL@eXamplE.Com</code>. For most use cases, set case sensitivity to <code>false</code> as a best practice. When usernames and email addresses are case insensitive, Amazon Cognito treats any variation in case as the same user, and prevents a case variation from being assigned to the same attribute for a different user.</p> <p>When <code>CaseSensitive</code> is <code>true</code> (case sensitive), Amazon Cognito interprets <code>USERNAME</code> and <code>UserName</code> as distinct users.</p> <p>This configuration is immutable after you set it.</p>"""
    account_recovery_setting: NotRequired[
        "aws_sdk_cognito_identity_provider.types.account_recovery_setting_type.AccountRecoverySettingType"
    ]
    """<p>The available verified method a user can use to recover their password when they call <code>ForgotPassword</code>. You can use this setting to define a preferred method when a user has more than one method available. With this setting, SMS doesn't qualify for a valid password recovery mechanism if the user also has SMS multi-factor authentication (MFA) activated. Email MFA is also disqualifying for account recovery with email. In the absence of this setting, Amazon Cognito uses the legacy behavior to determine the recovery method where SMS is preferred over email.</p> <p>As a best practice, configure both <code>verified_email</code> and <code>verified_phone_number</code>, with one having a higher priority than the other.</p>"""
    user_pool_tier: NotRequired[
        "aws_sdk_cognito_identity_provider.types.user_pool_tier_type.UserPoolTierType"
    ]
    r"""<p>The user pool <a href=\"https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-sign-in-feature-plans.html\">feature plan</a>, or tier. This parameter determines the eligibility of the user pool for features like managed login, access-token customization, and threat protection. Defaults to <code>ESSENTIALS</code>.</p>"""
    key_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.key_configuration_type.KeyConfigurationType"
    ]
    """<p>The key configuration for the user pool. Specifies the key type and KMS key ARN for encryption.</p>"""
    issuer_configuration: NotRequired[
        "aws_sdk_cognito_identity_provider.types.issuer_configuration_type.IssuerConfigurationType"
    ]
    """<p>The issuer configuration for the user pool. Specifies the issuer type for token generation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUserPoolRequest) -> dict:
    out: dict = {}
    out["PoolName"] = value["pool_name"]
    if "policies" in value:
        import aws_sdk_cognito_identity_provider.types.user_pool_policy_type

        out["Policies"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_policy_type.serialize_aws_json_1_1(
                value["policies"]
            )
        )
    if "deletion_protection" in value:
        import aws_sdk_cognito_identity_provider.types.deletion_protection_type

        out["DeletionProtection"] = (
            aws_sdk_cognito_identity_provider.types.deletion_protection_type.serialize_aws_json_1_1(
                value["deletion_protection"]
            )
        )
    if "lambda_config" in value:
        import aws_sdk_cognito_identity_provider.types.lambda_config_type

        out["LambdaConfig"] = (
            aws_sdk_cognito_identity_provider.types.lambda_config_type.serialize_aws_json_1_1(
                value["lambda_config"]
            )
        )
    if "auto_verified_attributes" in value:
        import aws_sdk_cognito_identity_provider.types.verified_attributes_list_type

        out["AutoVerifiedAttributes"] = (
            aws_sdk_cognito_identity_provider.types.verified_attributes_list_type.serialize_aws_json_1_1(
                value["auto_verified_attributes"]
            )
        )
    if "alias_attributes" in value:
        import aws_sdk_cognito_identity_provider.types.alias_attributes_list_type

        out["AliasAttributes"] = (
            aws_sdk_cognito_identity_provider.types.alias_attributes_list_type.serialize_aws_json_1_1(
                value["alias_attributes"]
            )
        )
    if "username_attributes" in value:
        import aws_sdk_cognito_identity_provider.types.username_attributes_list_type

        out["UsernameAttributes"] = (
            aws_sdk_cognito_identity_provider.types.username_attributes_list_type.serialize_aws_json_1_1(
                value["username_attributes"]
            )
        )
    if "sms_verification_message" in value:
        out["SmsVerificationMessage"] = value["sms_verification_message"]
    if "email_verification_message" in value:
        out["EmailVerificationMessage"] = value["email_verification_message"]
    if "email_verification_subject" in value:
        out["EmailVerificationSubject"] = value["email_verification_subject"]
    if "verification_message_template" in value:
        import aws_sdk_cognito_identity_provider.types.verification_message_template_type

        out["VerificationMessageTemplate"] = (
            aws_sdk_cognito_identity_provider.types.verification_message_template_type.serialize_aws_json_1_1(
                value["verification_message_template"]
            )
        )
    if "sms_authentication_message" in value:
        out["SmsAuthenticationMessage"] = value["sms_authentication_message"]
    if "mfa_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.user_pool_mfa_type

        out["MfaConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_mfa_type.serialize_aws_json_1_1(
                value["mfa_configuration"]
            )
        )
    if "user_attribute_update_settings" in value:
        import aws_sdk_cognito_identity_provider.types.user_attribute_update_settings_type

        out["UserAttributeUpdateSettings"] = (
            aws_sdk_cognito_identity_provider.types.user_attribute_update_settings_type.serialize_aws_json_1_1(
                value["user_attribute_update_settings"]
            )
        )
    if "device_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.device_configuration_type

        out["DeviceConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.device_configuration_type.serialize_aws_json_1_1(
                value["device_configuration"]
            )
        )
    if "email_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.email_configuration_type

        out["EmailConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.email_configuration_type.serialize_aws_json_1_1(
                value["email_configuration"]
            )
        )
    if "sms_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.sms_configuration_type

        out["SmsConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.sms_configuration_type.serialize_aws_json_1_1(
                value["sms_configuration"]
            )
        )
    if "user_pool_tags" in value:
        import aws_sdk_cognito_identity_provider.types.user_pool_tags_type

        out["UserPoolTags"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_tags_type.serialize_aws_json_1_1(
                value["user_pool_tags"]
            )
        )
    if "admin_create_user_config" in value:
        import aws_sdk_cognito_identity_provider.types.admin_create_user_config_type

        out["AdminCreateUserConfig"] = (
            aws_sdk_cognito_identity_provider.types.admin_create_user_config_type.serialize_aws_json_1_1(
                value["admin_create_user_config"]
            )
        )
    if "schema" in value:
        import aws_sdk_cognito_identity_provider.types.schema_attributes_list_type

        out["Schema"] = (
            aws_sdk_cognito_identity_provider.types.schema_attributes_list_type.serialize_aws_json_1_1(
                value["schema"]
            )
        )
    if "user_pool_add_ons" in value:
        import aws_sdk_cognito_identity_provider.types.user_pool_add_ons_type

        out["UserPoolAddOns"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_add_ons_type.serialize_aws_json_1_1(
                value["user_pool_add_ons"]
            )
        )
    if "username_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.username_configuration_type

        out["UsernameConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.username_configuration_type.serialize_aws_json_1_1(
                value["username_configuration"]
            )
        )
    if "account_recovery_setting" in value:
        import aws_sdk_cognito_identity_provider.types.account_recovery_setting_type

        out["AccountRecoverySetting"] = (
            aws_sdk_cognito_identity_provider.types.account_recovery_setting_type.serialize_aws_json_1_1(
                value["account_recovery_setting"]
            )
        )
    if "user_pool_tier" in value:
        import aws_sdk_cognito_identity_provider.types.user_pool_tier_type

        out["UserPoolTier"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_tier_type.serialize_aws_json_1_1(
                value["user_pool_tier"]
            )
        )
    if "key_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.key_configuration_type

        out["KeyConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.key_configuration_type.serialize_aws_json_1_1(
                value["key_configuration"]
            )
        )
    if "issuer_configuration" in value:
        import aws_sdk_cognito_identity_provider.types.issuer_configuration_type

        out["IssuerConfiguration"] = (
            aws_sdk_cognito_identity_provider.types.issuer_configuration_type.serialize_aws_json_1_1(
                value["issuer_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUserPoolRequest:
    out: CreateUserPoolRequest = {}  # type: ignore[typeddict-item]
    if "PoolName" in data:
        out["pool_name"] = data["PoolName"]
    else:
        raise DeserializationError("CreateUserPoolRequest.pool_name required")
    if "Policies" in data:
        import aws_sdk_cognito_identity_provider.types.user_pool_policy_type

        out["policies"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_policy_type.deserialize_aws_json_1_1(
                data["Policies"]
            )
        )
    if "DeletionProtection" in data:
        import aws_sdk_cognito_identity_provider.types.deletion_protection_type

        out["deletion_protection"] = (
            aws_sdk_cognito_identity_provider.types.deletion_protection_type.deserialize_aws_json_1_1(
                data["DeletionProtection"]
            )
        )
    if "LambdaConfig" in data:
        import aws_sdk_cognito_identity_provider.types.lambda_config_type

        out["lambda_config"] = (
            aws_sdk_cognito_identity_provider.types.lambda_config_type.deserialize_aws_json_1_1(
                data["LambdaConfig"]
            )
        )
    if "AutoVerifiedAttributes" in data:
        import aws_sdk_cognito_identity_provider.types.verified_attributes_list_type

        out["auto_verified_attributes"] = (
            aws_sdk_cognito_identity_provider.types.verified_attributes_list_type.deserialize_aws_json_1_1(
                data["AutoVerifiedAttributes"]
            )
        )
    if "AliasAttributes" in data:
        import aws_sdk_cognito_identity_provider.types.alias_attributes_list_type

        out["alias_attributes"] = (
            aws_sdk_cognito_identity_provider.types.alias_attributes_list_type.deserialize_aws_json_1_1(
                data["AliasAttributes"]
            )
        )
    if "UsernameAttributes" in data:
        import aws_sdk_cognito_identity_provider.types.username_attributes_list_type

        out["username_attributes"] = (
            aws_sdk_cognito_identity_provider.types.username_attributes_list_type.deserialize_aws_json_1_1(
                data["UsernameAttributes"]
            )
        )
    if "SmsVerificationMessage" in data:
        out["sms_verification_message"] = data["SmsVerificationMessage"]
    if "EmailVerificationMessage" in data:
        out["email_verification_message"] = data["EmailVerificationMessage"]
    if "EmailVerificationSubject" in data:
        out["email_verification_subject"] = data["EmailVerificationSubject"]
    if "VerificationMessageTemplate" in data:
        import aws_sdk_cognito_identity_provider.types.verification_message_template_type

        out["verification_message_template"] = (
            aws_sdk_cognito_identity_provider.types.verification_message_template_type.deserialize_aws_json_1_1(
                data["VerificationMessageTemplate"]
            )
        )
    if "SmsAuthenticationMessage" in data:
        out["sms_authentication_message"] = data["SmsAuthenticationMessage"]
    if "MfaConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.user_pool_mfa_type

        out["mfa_configuration"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_mfa_type.deserialize_aws_json_1_1(
                data["MfaConfiguration"]
            )
        )
    if "UserAttributeUpdateSettings" in data:
        import aws_sdk_cognito_identity_provider.types.user_attribute_update_settings_type

        out["user_attribute_update_settings"] = (
            aws_sdk_cognito_identity_provider.types.user_attribute_update_settings_type.deserialize_aws_json_1_1(
                data["UserAttributeUpdateSettings"]
            )
        )
    if "DeviceConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.device_configuration_type

        out["device_configuration"] = (
            aws_sdk_cognito_identity_provider.types.device_configuration_type.deserialize_aws_json_1_1(
                data["DeviceConfiguration"]
            )
        )
    if "EmailConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.email_configuration_type

        out["email_configuration"] = (
            aws_sdk_cognito_identity_provider.types.email_configuration_type.deserialize_aws_json_1_1(
                data["EmailConfiguration"]
            )
        )
    if "SmsConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.sms_configuration_type

        out["sms_configuration"] = (
            aws_sdk_cognito_identity_provider.types.sms_configuration_type.deserialize_aws_json_1_1(
                data["SmsConfiguration"]
            )
        )
    if "UserPoolTags" in data:
        import aws_sdk_cognito_identity_provider.types.user_pool_tags_type

        out["user_pool_tags"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_tags_type.deserialize_aws_json_1_1(
                data["UserPoolTags"]
            )
        )
    if "AdminCreateUserConfig" in data:
        import aws_sdk_cognito_identity_provider.types.admin_create_user_config_type

        out["admin_create_user_config"] = (
            aws_sdk_cognito_identity_provider.types.admin_create_user_config_type.deserialize_aws_json_1_1(
                data["AdminCreateUserConfig"]
            )
        )
    if "Schema" in data:
        import aws_sdk_cognito_identity_provider.types.schema_attributes_list_type

        out["schema"] = (
            aws_sdk_cognito_identity_provider.types.schema_attributes_list_type.deserialize_aws_json_1_1(
                data["Schema"]
            )
        )
    if "UserPoolAddOns" in data:
        import aws_sdk_cognito_identity_provider.types.user_pool_add_ons_type

        out["user_pool_add_ons"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_add_ons_type.deserialize_aws_json_1_1(
                data["UserPoolAddOns"]
            )
        )
    if "UsernameConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.username_configuration_type

        out["username_configuration"] = (
            aws_sdk_cognito_identity_provider.types.username_configuration_type.deserialize_aws_json_1_1(
                data["UsernameConfiguration"]
            )
        )
    if "AccountRecoverySetting" in data:
        import aws_sdk_cognito_identity_provider.types.account_recovery_setting_type

        out["account_recovery_setting"] = (
            aws_sdk_cognito_identity_provider.types.account_recovery_setting_type.deserialize_aws_json_1_1(
                data["AccountRecoverySetting"]
            )
        )
    if "UserPoolTier" in data:
        import aws_sdk_cognito_identity_provider.types.user_pool_tier_type

        out["user_pool_tier"] = (
            aws_sdk_cognito_identity_provider.types.user_pool_tier_type.deserialize_aws_json_1_1(
                data["UserPoolTier"]
            )
        )
    if "KeyConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.key_configuration_type

        out["key_configuration"] = (
            aws_sdk_cognito_identity_provider.types.key_configuration_type.deserialize_aws_json_1_1(
                data["KeyConfiguration"]
            )
        )
    if "IssuerConfiguration" in data:
        import aws_sdk_cognito_identity_provider.types.issuer_configuration_type

        out["issuer_configuration"] = (
            aws_sdk_cognito_identity_provider.types.issuer_configuration_type.deserialize_aws_json_1_1(
                data["IssuerConfiguration"]
            )
        )
    return out
