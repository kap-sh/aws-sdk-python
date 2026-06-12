"""Generated from Smithy shape ``com.amazonaws.appconfig#ConfigurationProfile``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.arn
    import aws_sdk_appconfig.types.configuration_profile_type
    import aws_sdk_appconfig.types.description
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.kms_key_identifier
    import aws_sdk_appconfig.types.long_name
    import aws_sdk_appconfig.types.role_arn
    import aws_sdk_appconfig.types.uri
    import aws_sdk_appconfig.types.validator_list


class ConfigurationProfile(TypedDict):
    application_id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The application ID.</p>"""
    id: NotRequired["aws_sdk_appconfig.types.id.Id"]
    """<p>The configuration profile ID.</p>"""
    name: NotRequired["aws_sdk_appconfig.types.long_name.LongName"]
    """<p>The name of the configuration profile.</p>"""
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>The configuration profile description.</p>"""
    location_uri: NotRequired["aws_sdk_appconfig.types.uri.Uri"]
    """<p>The URI location of the configuration.</p>"""
    retrieval_role_arn: NotRequired["aws_sdk_appconfig.types.role_arn.RoleArn"]
    """<p>The ARN of an IAM role with permission to access the configuration at the specified <code>LocationUri</code>.</p>"""
    validators: NotRequired["aws_sdk_appconfig.types.validator_list.ValidatorList"]
    """<p>A list of methods for validating the configuration.</p>"""
    type: NotRequired[
        "aws_sdk_appconfig.types.configuration_profile_type.ConfigurationProfileType"
    ]
    """<p>The type of configurations contained in the profile. AppConfig supports <code>feature flags</code> and <code>freeform</code> configurations. We recommend you create feature flag configurations to enable or disable new features and freeform configurations to distribute configurations to an application. When calling this API, enter one of the following values for <code>Type</code>:</p> <p> <code>AWS.AppConfig.FeatureFlags</code> </p> <p> <code>AWS.Freeform</code> </p>"""
    kms_key_arn: NotRequired["aws_sdk_appconfig.types.arn.Arn"]
    """<p>The Amazon Resource Name of the Key Management Service key to encrypt new configuration data versions in the AppConfig hosted configuration store. This attribute is only used for <code>hosted</code> configuration types. To encrypt data managed in other configuration stores, see the documentation for how to specify an KMS key for that particular service.</p>"""
    kms_key_identifier: NotRequired[
        "aws_sdk_appconfig.types.kms_key_identifier.KmsKeyIdentifier"
    ]
    """<p>The Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationProfile) -> dict:
    out: dict = {}
    if "application_id" in value:
        out["ApplicationId"] = value["application_id"]
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    if "retrieval_role_arn" in value:
        out["RetrievalRoleArn"] = value["retrieval_role_arn"]
    if "validators" in value:
        import aws_sdk_appconfig.types.validator_list

        out["Validators"] = aws_sdk_appconfig.types.validator_list.serialize_json(
            value["validators"]
        )
    if "type" in value:
        out["Type"] = value["type"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    return out


def deserialize_json(data: dict) -> ConfigurationProfile:
    out: ConfigurationProfile = {}  # type: ignore[typeddict-item]
    if "ApplicationId" in data:
        out["application_id"] = data["ApplicationId"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "LocationUri" in data:
        out["location_uri"] = data["LocationUri"]
    if "RetrievalRoleArn" in data:
        out["retrieval_role_arn"] = data["RetrievalRoleArn"]
    if "Validators" in data:
        import aws_sdk_appconfig.types.validator_list

        out["validators"] = aws_sdk_appconfig.types.validator_list.deserialize_json(
            data["Validators"]
        )
    if "Type" in data:
        out["type"] = data["Type"]
    if "KmsKeyArn" in data:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if "KmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    return out
