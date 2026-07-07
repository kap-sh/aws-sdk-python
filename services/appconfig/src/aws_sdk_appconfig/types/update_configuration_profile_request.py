"""Generated from Smithy shape ``com.amazonaws.appconfig#UpdateConfigurationProfileRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_appconfig.types.description
    import aws_sdk_appconfig.types.id
    import aws_sdk_appconfig.types.kms_key_identifier_or_empty
    import aws_sdk_appconfig.types.long_name
    import aws_sdk_appconfig.types.role_arn
    import aws_sdk_appconfig.types.validator_list


class UpdateConfigurationProfileRequest(TypedDict, closed=True):
    application_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The application ID.</p>"""
    configuration_profile_id: "aws_sdk_appconfig.types.id.Id"
    """<p>The ID of the configuration profile.</p>"""
    name: NotRequired["aws_sdk_appconfig.types.long_name.LongName"]
    """<p>The name of the configuration profile.</p>"""
    description: NotRequired["aws_sdk_appconfig.types.description.Description"]
    """<p>A description of the configuration profile.</p>"""
    retrieval_role_arn: NotRequired["aws_sdk_appconfig.types.role_arn.RoleArn"]
    """<p>The ARN of an IAM role with permission to access the configuration at the specified <code>LocationUri</code>.</p> <important> <p>A retrieval role ARN is not required for configurations stored in CodePipeline or the AppConfig hosted configuration store. It is required for all other sources that store your configuration. </p> </important>"""
    validators: NotRequired["aws_sdk_appconfig.types.validator_list.ValidatorList"]
    """<p>A list of methods for validating the configuration.</p>"""
    kms_key_identifier: NotRequired[
        "aws_sdk_appconfig.types.kms_key_identifier_or_empty.KmsKeyIdentifierOrEmpty"
    ]
    """<p>The identifier for a Key Management Service key to encrypt new configuration data versions in the AppConfig hosted configuration store. This attribute is only used for <code>hosted</code> configuration types. The identifier can be an KMS key ID, alias, or the Amazon Resource Name (ARN) of the key ID or alias. To encrypt data managed in other configuration stores, see the documentation for how to specify an KMS key for that particular service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationProfileRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "retrieval_role_arn" in value:
        out["RetrievalRoleArn"] = value["retrieval_role_arn"]
    if "validators" in value:
        import aws_sdk_appconfig.types.validator_list

        out["Validators"] = aws_sdk_appconfig.types.validator_list.serialize_json(
            value["validators"]
        )
    if "kms_key_identifier" in value:
        out["KmsKeyIdentifier"] = value["kms_key_identifier"]
    return out


def deserialize_json(data: dict) -> UpdateConfigurationProfileRequest:
    out: UpdateConfigurationProfileRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "RetrievalRoleArn" in data:
        out["retrieval_role_arn"] = data["RetrievalRoleArn"]
    if "Validators" in data:
        import aws_sdk_appconfig.types.validator_list

        out["validators"] = aws_sdk_appconfig.types.validator_list.deserialize_json(
            data["Validators"]
        )
    if "KmsKeyIdentifier" in data:
        out["kms_key_identifier"] = data["KmsKeyIdentifier"]
    return out
