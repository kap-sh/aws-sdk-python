"""Generated from Smithy shape ``com.amazonaws.inspector2#CodeSecurityScanConfigurationSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector2.types.continuous_integration_scan_supported_events
    import aws_sdk_inspector2.types.frequency_expression
    import aws_sdk_inspector2.types.owner_id
    import aws_sdk_inspector2.types.periodic_scan_frequency
    import aws_sdk_inspector2.types.rule_set_categories
    import aws_sdk_inspector2.types.scan_configuration_arn
    import aws_sdk_inspector2.types.scan_configuration_name
    import aws_sdk_inspector2.types.scope_settings
    import aws_sdk_inspector2.types.tag_map


class CodeSecurityScanConfigurationSummary(TypedDict):
    scan_configuration_arn: (
        "aws_sdk_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the scan configuration.</p>"""
    name: "aws_sdk_inspector2.types.scan_configuration_name.ScanConfigurationName"
    """<p>The name of the scan configuration.</p>"""
    owner_account_id: "aws_sdk_inspector2.types.owner_id.OwnerId"
    """<p>The Amazon Web Services account ID that owns the scan configuration.</p>"""
    periodic_scan_frequency: NotRequired[
        "aws_sdk_inspector2.types.periodic_scan_frequency.PeriodicScanFrequency"
    ]
    """<p>The frequency at which periodic scans are performed.</p>"""
    frequency_expression: NotRequired[
        "aws_sdk_inspector2.types.frequency_expression.FrequencyExpression"
    ]
    """<p>The schedule expression for periodic scans, in cron format.</p>"""
    continuous_integration_scan_supported_events: NotRequired[
        "aws_sdk_inspector2.types.continuous_integration_scan_supported_events.ContinuousIntegrationScanSupportedEvents"
    ]
    """<p>The repository events that trigger continuous integration scans.</p>"""
    rule_set_categories: (
        "aws_sdk_inspector2.types.rule_set_categories.RuleSetCategories"
    )
    """<p>The categories of security rules applied during the scan.</p>"""
    scope_settings: NotRequired["aws_sdk_inspector2.types.scope_settings.ScopeSettings"]
    """<p>The scope settings that define which repositories will be scanned. If the <code>ScopeSetting</code> parameter is <code>ALL</code> the scan configuration applies to all existing and future projects imported into Amazon Inspector.</p>"""
    tags: NotRequired["aws_sdk_inspector2.types.tag_map.TagMap"]
    """<p>The tags associated with the scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeSecurityScanConfigurationSummary) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    out["name"] = value["name"]
    out["ownerAccountId"] = value["owner_account_id"]
    if "periodic_scan_frequency" in value:
        import aws_sdk_inspector2.types.periodic_scan_frequency

        out["periodicScanFrequency"] = (
            aws_sdk_inspector2.types.periodic_scan_frequency.serialize_json(
                value["periodic_scan_frequency"]
            )
        )
    if "frequency_expression" in value:
        out["frequencyExpression"] = value["frequency_expression"]
    if "continuous_integration_scan_supported_events" in value:
        import aws_sdk_inspector2.types.continuous_integration_scan_supported_events

        out["continuousIntegrationScanSupportedEvents"] = (
            aws_sdk_inspector2.types.continuous_integration_scan_supported_events.serialize_json(
                value["continuous_integration_scan_supported_events"]
            )
        )
    import aws_sdk_inspector2.types.rule_set_categories

    out["ruleSetCategories"] = (
        aws_sdk_inspector2.types.rule_set_categories.serialize_json(
            value["rule_set_categories"]
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


def deserialize_json(data: dict) -> CodeSecurityScanConfigurationSummary:
    out: CodeSecurityScanConfigurationSummary = {}  # type: ignore[typeddict-item]
    if "scanConfigurationArn" in data:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        raise DeserializationError(
            "CodeSecurityScanConfigurationSummary.scan_configuration_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CodeSecurityScanConfigurationSummary.name required")
    if "ownerAccountId" in data:
        out["owner_account_id"] = data["ownerAccountId"]
    else:
        raise DeserializationError(
            "CodeSecurityScanConfigurationSummary.owner_account_id required"
        )
    if "periodicScanFrequency" in data:
        import aws_sdk_inspector2.types.periodic_scan_frequency

        out["periodic_scan_frequency"] = (
            aws_sdk_inspector2.types.periodic_scan_frequency.deserialize_json(
                data["periodicScanFrequency"]
            )
        )
    if "frequencyExpression" in data:
        out["frequency_expression"] = data["frequencyExpression"]
    if "continuousIntegrationScanSupportedEvents" in data:
        import aws_sdk_inspector2.types.continuous_integration_scan_supported_events

        out["continuous_integration_scan_supported_events"] = (
            aws_sdk_inspector2.types.continuous_integration_scan_supported_events.deserialize_json(
                data["continuousIntegrationScanSupportedEvents"]
            )
        )
    if "ruleSetCategories" in data:
        import aws_sdk_inspector2.types.rule_set_categories

        out["rule_set_categories"] = (
            aws_sdk_inspector2.types.rule_set_categories.deserialize_json(
                data["ruleSetCategories"]
            )
        )
    else:
        raise DeserializationError(
            "CodeSecurityScanConfigurationSummary.rule_set_categories required"
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
