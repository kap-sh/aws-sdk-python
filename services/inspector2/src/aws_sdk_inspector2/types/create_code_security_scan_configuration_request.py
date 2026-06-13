"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateCodeSecurityScanConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.code_security_scan_configuration
    import aws_sdk_inspector2.types.configuration_level
    import aws_sdk_inspector2.types.scan_configuration_name
    import aws_sdk_inspector2.types.scope_settings
    import aws_sdk_inspector2.types.tag_map


class CreateCodeSecurityScanConfigurationRequest(TypedDict):
    name: "aws_sdk_inspector2.types.scan_configuration_name.ScanConfigurationName"
    """<p>The name of the scan configuration.</p>"""
    level: "aws_sdk_inspector2.types.configuration_level.ConfigurationLevel"
    """<p>The security level for the scan configuration.</p>"""
    configuration: "aws_sdk_inspector2.types.code_security_scan_configuration.CodeSecurityScanConfiguration"
    """<p>The configuration settings for the code security scan.</p>"""
    scope_settings: NotRequired["aws_sdk_inspector2.types.scope_settings.ScopeSettings"]
    """<p>The scope settings that define which repositories will be scanned. Include this parameter to create a default scan configuration. Otherwise Amazon Inspector creates a general scan configuration. </p> <p>A default scan configuration automatically applies to all existing and future projects imported into Amazon Inspector. Use the <code>BatchAssociateCodeSecurityScanConfiguration</code> operation to associate a general scan configuration with projects.</p>"""
    tags: NotRequired["aws_sdk_inspector2.types.tag_map.TagMap"]
    """<p>The tags to apply to the scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeSecurityScanConfigurationRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import aws_sdk_inspector2.types.configuration_level

    out["level"] = aws_sdk_inspector2.types.configuration_level.serialize_json(
        value["level"]
    )
    import aws_sdk_inspector2.types.code_security_scan_configuration

    out["configuration"] = (
        aws_sdk_inspector2.types.code_security_scan_configuration.serialize_json(
            value["configuration"]
        )
    )
    if "scope_settings" in value:
        import aws_sdk_inspector2.types.scope_settings

        out["scopeSettings"] = aws_sdk_inspector2.types.scope_settings.serialize_json(
            value["scope_settings"]
        )
    if "tags" in value:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateCodeSecurityScanConfigurationRequest:
    out: CreateCodeSecurityScanConfigurationRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "CreateCodeSecurityScanConfigurationRequest.name required"
        )
    if "level" in data:
        import aws_sdk_inspector2.types.configuration_level

        out["level"] = aws_sdk_inspector2.types.configuration_level.deserialize_json(
            data["level"]
        )
    else:
        raise DeserializationError(
            "CreateCodeSecurityScanConfigurationRequest.level required"
        )
    if "configuration" in data:
        import aws_sdk_inspector2.types.code_security_scan_configuration

        out["configuration"] = (
            aws_sdk_inspector2.types.code_security_scan_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCodeSecurityScanConfigurationRequest.configuration required"
        )
    if "scopeSettings" in data:
        import aws_sdk_inspector2.types.scope_settings

        out["scope_settings"] = (
            aws_sdk_inspector2.types.scope_settings.deserialize_json(
                data["scopeSettings"]
            )
        )
    if "tags" in data:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.deserialize_json(data["tags"])
    return out
