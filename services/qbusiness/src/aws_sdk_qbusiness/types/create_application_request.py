"""Generated from Smithy shape ``com.amazonaws.qbusiness#CreateApplicationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.application_name
    import aws_sdk_qbusiness.types.attachments_configuration
    import aws_sdk_qbusiness.types.client_ids_for_oidc
    import aws_sdk_qbusiness.types.client_token
    import aws_sdk_qbusiness.types.description
    import aws_sdk_qbusiness.types.encryption_configuration
    import aws_sdk_qbusiness.types.iam_identity_provider_arn
    import aws_sdk_qbusiness.types.identity_type
    import aws_sdk_qbusiness.types.instance_arn
    import aws_sdk_qbusiness.types.personalization_configuration
    import aws_sdk_qbusiness.types.q_apps_configuration
    import aws_sdk_qbusiness.types.quick_sight_configuration
    import aws_sdk_qbusiness.types.role_arn
    import aws_sdk_qbusiness.types.tags


class CreateApplicationRequest(TypedDict):
    display_name: "aws_sdk_qbusiness.types.application_name.ApplicationName"
    """<p>A name for the Amazon Q Business application. </p>"""
    role_arn: NotRequired["aws_sdk_qbusiness.types.role_arn.RoleArn"]
    r"""<p> The Amazon Resource Name (ARN) of an IAM role with permissions to access your Amazon CloudWatch logs and metrics. If this property is not specified, Amazon Q Business will create a <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles.html#slr-permissions\">service linked role (SLR)</a> and use it as the application's role.</p>"""
    identity_type: NotRequired["aws_sdk_qbusiness.types.identity_type.IdentityType"]
    """<p>The authentication type being used by a Amazon Q Business application.</p>"""
    iam_identity_provider_arn: NotRequired[
        "aws_sdk_qbusiness.types.iam_identity_provider_arn.IAMIdentityProviderArn"
    ]
    """<p>The Amazon Resource Name (ARN) of an identity provider being used by an Amazon Q Business application.</p>"""
    identity_center_instance_arn: NotRequired[
        "aws_sdk_qbusiness.types.instance_arn.InstanceArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating for—or connecting to—your Amazon Q Business application.</p>"""
    client_ids_for_oidc: NotRequired[
        "aws_sdk_qbusiness.types.client_ids_for_oidc.ClientIdsForOIDC"
    ]
    """<p>The OIDC client ID for a Amazon Q Business application.</p>"""
    description: NotRequired["aws_sdk_qbusiness.types.description.Description"]
    """<p>A description for the Amazon Q Business application. </p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_qbusiness.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The identifier of the KMS key that is used to encrypt your data. Amazon Q Business doesn't support asymmetric keys.</p>"""
    tags: NotRequired["aws_sdk_qbusiness.types.tags.Tags"]
    """<p>A list of key-value pairs that identify or categorize your Amazon Q Business application. You can also use tags to help control access to the application. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>"""
    client_token: NotRequired["aws_sdk_qbusiness.types.client_token.ClientToken"]
    """<p>A token that you provide to identify the request to create your Amazon Q Business application.</p>"""
    attachments_configuration: NotRequired[
        "aws_sdk_qbusiness.types.attachments_configuration.AttachmentsConfiguration"
    ]
    """<p>An option to allow end users to upload files directly during chat.</p>"""
    q_apps_configuration: NotRequired[
        "aws_sdk_qbusiness.types.q_apps_configuration.QAppsConfiguration"
    ]
    """<p>An option to allow end users to create and use Amazon Q Apps in the web experience.</p>"""
    personalization_configuration: NotRequired[
        "aws_sdk_qbusiness.types.personalization_configuration.PersonalizationConfiguration"
    ]
    r"""<p>Configuration information about chat response personalization. For more information, see <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html\">Personalizing chat responses</a> </p>"""
    quick_sight_configuration: NotRequired[
        "aws_sdk_qbusiness.types.quick_sight_configuration.QuickSightConfiguration"
    ]
    r"""<p>The Amazon Quick Suite configuration for an Amazon Q Business application that uses Quick Suite for authentication. This configuration is required if your application uses Quick Suite as the identity provider. For more information, see <a href=\"https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-quicksight-integrated-application.html\">Creating an Amazon Quick Suite integrated application</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateApplicationRequest) -> dict:
    out: dict = {}
    out["displayName"] = value["display_name"]
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "identity_type" in value:
        import aws_sdk_qbusiness.types.identity_type

        out["identityType"] = aws_sdk_qbusiness.types.identity_type.serialize_json(
            value["identity_type"]
        )
    if "iam_identity_provider_arn" in value:
        out["iamIdentityProviderArn"] = value["iam_identity_provider_arn"]
    if "identity_center_instance_arn" in value:
        out["identityCenterInstanceArn"] = value["identity_center_instance_arn"]
    if "client_ids_for_oidc" in value:
        import aws_sdk_qbusiness.types.client_ids_for_oidc

        out["clientIdsForOIDC"] = (
            aws_sdk_qbusiness.types.client_ids_for_oidc.serialize_json(
                value["client_ids_for_oidc"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "encryption_configuration" in value:
        import aws_sdk_qbusiness.types.encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_qbusiness.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_qbusiness.types.tags

        out["tags"] = aws_sdk_qbusiness.types.tags.serialize_json(value["tags"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "attachments_configuration" in value:
        import aws_sdk_qbusiness.types.attachments_configuration

        out["attachmentsConfiguration"] = (
            aws_sdk_qbusiness.types.attachments_configuration.serialize_json(
                value["attachments_configuration"]
            )
        )
    if "q_apps_configuration" in value:
        import aws_sdk_qbusiness.types.q_apps_configuration

        out["qAppsConfiguration"] = (
            aws_sdk_qbusiness.types.q_apps_configuration.serialize_json(
                value["q_apps_configuration"]
            )
        )
    if "personalization_configuration" in value:
        import aws_sdk_qbusiness.types.personalization_configuration

        out["personalizationConfiguration"] = (
            aws_sdk_qbusiness.types.personalization_configuration.serialize_json(
                value["personalization_configuration"]
            )
        )
    if "quick_sight_configuration" in value:
        import aws_sdk_qbusiness.types.quick_sight_configuration

        out["quickSightConfiguration"] = (
            aws_sdk_qbusiness.types.quick_sight_configuration.serialize_json(
                value["quick_sight_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateApplicationRequest:
    out: CreateApplicationRequest = {}  # type: ignore[typeddict-item]
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    else:
        raise DeserializationError("CreateApplicationRequest.display_name required")
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "identityType" in data:
        import aws_sdk_qbusiness.types.identity_type

        out["identity_type"] = aws_sdk_qbusiness.types.identity_type.deserialize_json(
            data["identityType"]
        )
    if "iamIdentityProviderArn" in data:
        out["iam_identity_provider_arn"] = data["iamIdentityProviderArn"]
    if "identityCenterInstanceArn" in data:
        out["identity_center_instance_arn"] = data["identityCenterInstanceArn"]
    if "clientIdsForOIDC" in data:
        import aws_sdk_qbusiness.types.client_ids_for_oidc

        out["client_ids_for_oidc"] = (
            aws_sdk_qbusiness.types.client_ids_for_oidc.deserialize_json(
                data["clientIdsForOIDC"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "encryptionConfiguration" in data:
        import aws_sdk_qbusiness.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_qbusiness.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_qbusiness.types.tags

        out["tags"] = aws_sdk_qbusiness.types.tags.deserialize_json(data["tags"])
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "attachmentsConfiguration" in data:
        import aws_sdk_qbusiness.types.attachments_configuration

        out["attachments_configuration"] = (
            aws_sdk_qbusiness.types.attachments_configuration.deserialize_json(
                data["attachmentsConfiguration"]
            )
        )
    if "qAppsConfiguration" in data:
        import aws_sdk_qbusiness.types.q_apps_configuration

        out["q_apps_configuration"] = (
            aws_sdk_qbusiness.types.q_apps_configuration.deserialize_json(
                data["qAppsConfiguration"]
            )
        )
    if "personalizationConfiguration" in data:
        import aws_sdk_qbusiness.types.personalization_configuration

        out["personalization_configuration"] = (
            aws_sdk_qbusiness.types.personalization_configuration.deserialize_json(
                data["personalizationConfiguration"]
            )
        )
    if "quickSightConfiguration" in data:
        import aws_sdk_qbusiness.types.quick_sight_configuration

        out["quick_sight_configuration"] = (
            aws_sdk_qbusiness.types.quick_sight_configuration.deserialize_json(
                data["quickSightConfiguration"]
            )
        )
    return out
