"""Generated from Smithy shape ``com.amazonaws.workspacesweb#IpAccessSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.arn_list
    import aws_sdk_workspaces_web.types.description
    import aws_sdk_workspaces_web.types.display_name
    import aws_sdk_workspaces_web.types.encryption_context_map
    import aws_sdk_workspaces_web.types.ip_rule_list
    import aws_sdk_workspaces_web.types.key_arn
    import aws_sdk_workspaces_web.types.timestamp


class IpAccessSettings(TypedDict, closed=True):
    ip_access_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the IP access settings resource.</p>"""
    associated_portal_arns: NotRequired["aws_sdk_workspaces_web.types.arn_list.ArnList"]
    """<p>A list of web portal ARNs that this IP access settings resource is associated with.</p>"""
    ip_rules: NotRequired["aws_sdk_workspaces_web.types.ip_rule_list.IpRuleList"]
    """<p>The IP rules of the IP access settings.</p>"""
    display_name: NotRequired["aws_sdk_workspaces_web.types.display_name.DisplayName"]
    """<p> The display name of the IP access settings.</p>"""
    description: NotRequired["aws_sdk_workspaces_web.types.description.Description"]
    """<p>The description of the IP access settings.</p>"""
    creation_date: NotRequired["aws_sdk_workspaces_web.types.timestamp.Timestamp"]
    """<p>The creation date timestamp of the IP access settings.</p>"""
    customer_managed_key: NotRequired["aws_sdk_workspaces_web.types.key_arn.keyArn"]
    """<p>The customer managed key used to encrypt sensitive information in the IP access settings.</p>"""
    additional_encryption_context: NotRequired[
        "aws_sdk_workspaces_web.types.encryption_context_map.EncryptionContextMap"
    ]
    """<p>The additional encryption context of the IP access settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IpAccessSettings) -> dict:
    out: dict = {}
    out["ipAccessSettingsArn"] = value["ip_access_settings_arn"]
    if "associated_portal_arns" in value:
        import aws_sdk_workspaces_web.types.arn_list

        out["associatedPortalArns"] = (
            aws_sdk_workspaces_web.types.arn_list.serialize_json(
                value["associated_portal_arns"]
            )
        )
    if "ip_rules" in value:
        import aws_sdk_workspaces_web.types.ip_rule_list

        out["ipRules"] = aws_sdk_workspaces_web.types.ip_rule_list.serialize_json(
            value["ip_rules"]
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


def deserialize_json(data: dict) -> IpAccessSettings:
    out: IpAccessSettings = {}  # type: ignore[typeddict-item]
    if "ipAccessSettingsArn" in data:
        out["ip_access_settings_arn"] = data["ipAccessSettingsArn"]
    else:
        raise DeserializationError("IpAccessSettings.ip_access_settings_arn required")
    if "associatedPortalArns" in data:
        import aws_sdk_workspaces_web.types.arn_list

        out["associated_portal_arns"] = (
            aws_sdk_workspaces_web.types.arn_list.deserialize_json(
                data["associatedPortalArns"]
            )
        )
    if "ipRules" in data:
        import aws_sdk_workspaces_web.types.ip_rule_list

        out["ip_rules"] = aws_sdk_workspaces_web.types.ip_rule_list.deserialize_json(
            data["ipRules"]
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
