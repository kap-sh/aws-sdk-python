"""Generated from Smithy shape ``com.amazonaws.workspacesweb#BrowserSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn
    import aws_sdk_workspaces_web.types.arn_list
    import aws_sdk_workspaces_web.types.browser_policy
    import aws_sdk_workspaces_web.types.encryption_context_map
    import aws_sdk_workspaces_web.types.key_arn
    import aws_sdk_workspaces_web.types.web_content_filtering_policy


class BrowserSettings(TypedDict, closed=True):
    browser_settings_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the browser settings.</p>"""
    associated_portal_arns: NotRequired["aws_sdk_workspaces_web.types.arn_list.ArnList"]
    """<p>A list of web portal ARNs that this browser settings is associated with.</p>"""
    browser_policy: NotRequired[
        "aws_sdk_workspaces_web.types.browser_policy.BrowserPolicy"
    ]
    """<p>A JSON string containing Chrome Enterprise policies that will be applied to all streaming sessions.</p>"""
    customer_managed_key: NotRequired["aws_sdk_workspaces_web.types.key_arn.keyArn"]
    """<p>The customer managed key used to encrypt sensitive information in the browser settings.</p>"""
    additional_encryption_context: NotRequired[
        "aws_sdk_workspaces_web.types.encryption_context_map.EncryptionContextMap"
    ]
    """<p>The additional encryption context of the browser settings.</p>"""
    web_content_filtering_policy: NotRequired[
        "aws_sdk_workspaces_web.types.web_content_filtering_policy.WebContentFilteringPolicy"
    ]
    """<p>The policy that specifies which URLs end users are allowed to access or which URLs or domain categories they are restricted from accessing for enhanced security.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserSettings) -> dict:
    out: dict = {}
    out["browserSettingsArn"] = value["browser_settings_arn"]
    if "associated_portal_arns" in value:
        import aws_sdk_workspaces_web.types.arn_list

        out["associatedPortalArns"] = (
            aws_sdk_workspaces_web.types.arn_list.serialize_json(
                value["associated_portal_arns"]
            )
        )
    if "browser_policy" in value:
        out["browserPolicy"] = value["browser_policy"]
    if "customer_managed_key" in value:
        out["customerManagedKey"] = value["customer_managed_key"]
    if "additional_encryption_context" in value:
        import aws_sdk_workspaces_web.types.encryption_context_map

        out["additionalEncryptionContext"] = (
            aws_sdk_workspaces_web.types.encryption_context_map.serialize_json(
                value["additional_encryption_context"]
            )
        )
    if "web_content_filtering_policy" in value:
        import aws_sdk_workspaces_web.types.web_content_filtering_policy

        out["webContentFilteringPolicy"] = (
            aws_sdk_workspaces_web.types.web_content_filtering_policy.serialize_json(
                value["web_content_filtering_policy"]
            )
        )
    return out


def deserialize_json(data: dict) -> BrowserSettings:
    out: BrowserSettings = {}  # type: ignore[typeddict-item]
    if "browserSettingsArn" in data:
        out["browser_settings_arn"] = data["browserSettingsArn"]
    else:
        raise DeserializationError("BrowserSettings.browser_settings_arn required")
    if "associatedPortalArns" in data:
        import aws_sdk_workspaces_web.types.arn_list

        out["associated_portal_arns"] = (
            aws_sdk_workspaces_web.types.arn_list.deserialize_json(
                data["associatedPortalArns"]
            )
        )
    if "browserPolicy" in data:
        out["browser_policy"] = data["browserPolicy"]
    if "customerManagedKey" in data:
        out["customer_managed_key"] = data["customerManagedKey"]
    if "additionalEncryptionContext" in data:
        import aws_sdk_workspaces_web.types.encryption_context_map

        out["additional_encryption_context"] = (
            aws_sdk_workspaces_web.types.encryption_context_map.deserialize_json(
                data["additionalEncryptionContext"]
            )
        )
    if "webContentFilteringPolicy" in data:
        import aws_sdk_workspaces_web.types.web_content_filtering_policy

        out["web_content_filtering_policy"] = (
            aws_sdk_workspaces_web.types.web_content_filtering_policy.deserialize_json(
                data["webContentFilteringPolicy"]
            )
        )
    return out
