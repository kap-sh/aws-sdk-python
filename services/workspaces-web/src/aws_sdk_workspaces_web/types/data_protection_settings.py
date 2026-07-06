"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DataProtectionSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.arn_list
    import aws_sdk_workspaces_web.types.description_safe
    import aws_sdk_workspaces_web.types.display_name_safe
    import aws_sdk_workspaces_web.types.encryption_context_map
    import aws_sdk_workspaces_web.types.inline_redaction_configuration
    import aws_sdk_workspaces_web.types.key_arn
    import aws_sdk_workspaces_web.types.timestamp


class DataProtectionSettings(TypedDict, closed=True):
    data_protection_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the data protection settings resource.</p>"""
    inline_redaction_configuration: NotRequired[
        "aws_sdk_workspaces_web.types.inline_redaction_configuration.InlineRedactionConfiguration"
    ]
    """<p>The inline redaction configuration for the data protection settings.</p>"""
    associated_portal_arns: NotRequired["aws_sdk_workspaces_web.types.arn_list.ArnList"]
    """<p>A list of web portal ARNs that this data protection settings resource is associated with.</p>"""
    display_name: NotRequired[
        "aws_sdk_workspaces_web.types.display_name_safe.DisplayNameSafe"
    ]
    """<p>The display name of the data protection settings.</p>"""
    description: NotRequired[
        "aws_sdk_workspaces_web.types.description_safe.DescriptionSafe"
    ]
    """<p>The description of the data protection settings.</p>"""
    creation_date: NotRequired["aws_sdk_workspaces_web.types.timestamp.Timestamp"]
    """<p>The creation date timestamp of the data protection settings.</p>"""
    customer_managed_key: NotRequired["aws_sdk_workspaces_web.types.key_arn.keyArn"]
    """<p>The customer managed key used to encrypt sensitive information in the data protection settings.</p>"""
    additional_encryption_context: NotRequired[
        "aws_sdk_workspaces_web.types.encryption_context_map.EncryptionContextMap"
    ]
    """<p>The additional encryption context of the data protection settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataProtectionSettings) -> dict:
    out: dict = {}
    out["dataProtectionSettingsArn"] = value["data_protection_settings_arn"]
    if "inline_redaction_configuration" in value:
        import aws_sdk_workspaces_web.types.inline_redaction_configuration

        out["inlineRedactionConfiguration"] = (
            aws_sdk_workspaces_web.types.inline_redaction_configuration.serialize_json(
                value["inline_redaction_configuration"]
            )
        )
    if "associated_portal_arns" in value:
        import aws_sdk_workspaces_web.types.arn_list

        out["associatedPortalArns"] = (
            aws_sdk_workspaces_web.types.arn_list.serialize_json(
                value["associated_portal_arns"]
            )
        )
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    if "creation_date" in value:
        import aws_sdk_workspaces_web.types.timestamp

        out["creationDate"] = aws_sdk_workspaces_web.types.timestamp.serialize_json(
            value["creation_date"]
        )
    if "customer_managed_key" in value:
        out["customerManagedKey"] = value["customer_managed_key"]
    if "additional_encryption_context" in value:
        import aws_sdk_workspaces_web.types.encryption_context_map

        out["additionalEncryptionContext"] = (
            aws_sdk_workspaces_web.types.encryption_context_map.serialize_json(
                value["additional_encryption_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataProtectionSettings:
    out: DataProtectionSettings = {}  # type: ignore[typeddict-item]
    if "dataProtectionSettingsArn" in data:
        out["data_protection_settings_arn"] = data["dataProtectionSettingsArn"]
    else:
        raise DeserializationError(
            "DataProtectionSettings.data_protection_settings_arn required"
        )
    if "inlineRedactionConfiguration" in data:
        import aws_sdk_workspaces_web.types.inline_redaction_configuration

        out["inline_redaction_configuration"] = (
            aws_sdk_workspaces_web.types.inline_redaction_configuration.deserialize_json(
                data["inlineRedactionConfiguration"]
            )
        )
    if "associatedPortalArns" in data:
        import aws_sdk_workspaces_web.types.arn_list

        out["associated_portal_arns"] = (
            aws_sdk_workspaces_web.types.arn_list.deserialize_json(
                data["associatedPortalArns"]
            )
        )
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "description" in data:
        out["description"] = data["description"]
    if "creationDate" in data:
        import aws_sdk_workspaces_web.types.timestamp

        out["creation_date"] = aws_sdk_workspaces_web.types.timestamp.deserialize_json(
            data["creationDate"]
        )
    if "customerManagedKey" in data:
        out["customer_managed_key"] = data["customerManagedKey"]
    if "additionalEncryptionContext" in data:
        import aws_sdk_workspaces_web.types.encryption_context_map

        out["additional_encryption_context"] = (
            aws_sdk_workspaces_web.types.encryption_context_map.deserialize_json(
                data["additionalEncryptionContext"]
            )
        )
    return out
