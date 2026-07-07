"""Generated from Smithy shape ``com.amazonaws.inspector2#GetCodeSecurityScanConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_inspector2.types.code_security_scan_configuration
    import aws_sdk_inspector2.types.configuration_level
    import aws_sdk_inspector2.types.scan_configuration_arn
    import aws_sdk_inspector2.types.scan_configuration_name
    import aws_sdk_inspector2.types.scope_settings
    import aws_sdk_inspector2.types.tag_map


class GetCodeSecurityScanConfigurationResponse(TypedDict, closed=True):
    scan_configuration_arn: NotRequired[
        "aws_sdk_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the scan configuration.</p>"""
    name: NotRequired[
        "aws_sdk_inspector2.types.scan_configuration_name.ScanConfigurationName"
    ]
    """<p>The name of the scan configuration.</p>"""
    configuration: NotRequired[
        "aws_sdk_inspector2.types.code_security_scan_configuration.CodeSecurityScanConfiguration"
    ]
    """<p>The configuration settings for the code security scan.</p>"""
    level: NotRequired[
        "aws_sdk_inspector2.types.configuration_level.ConfigurationLevel"
    ]
    """<p>The security level for the scan configuration.</p>"""
    scope_settings: NotRequired["aws_sdk_inspector2.types.scope_settings.ScopeSettings"]
    """<p>The scope settings that define which repositories will be scanned. If the <code>ScopeSetting</code> parameter is <code>ALL</code> the scan configuration applies to all existing and future projects imported into Amazon Inspector.</p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the scan configuration was created.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The timestamp when the scan configuration was last updated.</p>"""
    tags: NotRequired["aws_sdk_inspector2.types.tag_map.TagMap"]
    """<p>The tags associated with the scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeSecurityScanConfigurationResponse) -> dict:
    out: dict = {}
    if "scan_configuration_arn" in value:
        out["scanConfigurationArn"] = value["scan_configuration_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "configuration" in value:
        import aws_sdk_inspector2.types.code_security_scan_configuration

        out["configuration"] = (
            aws_sdk_inspector2.types.code_security_scan_configuration.serialize_json(
                value["configuration"]
            )
        )
    if "level" in value:
        import aws_sdk_inspector2.types.configuration_level

        out["level"] = aws_sdk_inspector2.types.configuration_level.serialize_json(
            value["level"]
        )
    if "scope_settings" in value:
        import aws_sdk_inspector2.types.scope_settings

        out["scopeSettings"] = aws_sdk_inspector2.types.scope_settings.serialize_json(
            value["scope_settings"]
        )
    if "created_at" in value:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["createdAt"] = aws_sdk_inspector2.types._prelude.timestamp.serialize_json(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["lastUpdatedAt"] = (
            aws_sdk_inspector2.types._prelude.timestamp.serialize_json(
                value["last_updated_at"]
            )
        )
    if "tags" in value:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetCodeSecurityScanConfigurationResponse:
    out: GetCodeSecurityScanConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    if "name" in data:
        out["name"] = data["name"]
    if "configuration" in data:
        import aws_sdk_inspector2.types.code_security_scan_configuration

        out["configuration"] = (
            aws_sdk_inspector2.types.code_security_scan_configuration.deserialize_json(
                data["configuration"]
            )
        )
    if "level" in data:
        import aws_sdk_inspector2.types.configuration_level

        out["level"] = aws_sdk_inspector2.types.configuration_level.deserialize_json(
            data["level"]
        )
    if "scopeSettings" in data:
        import aws_sdk_inspector2.types.scope_settings

        out["scope_settings"] = (
            aws_sdk_inspector2.types.scope_settings.deserialize_json(
                data["scopeSettings"]
            )
        )
    if "createdAt" in data:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_inspector2.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_inspector2.types._prelude.timestamp

        out["last_updated_at"] = (
            aws_sdk_inspector2.types._prelude.timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    if "tags" in data:
        import aws_sdk_inspector2.types.tag_map

        out["tags"] = aws_sdk_inspector2.types.tag_map.deserialize_json(data["tags"])
    return out
