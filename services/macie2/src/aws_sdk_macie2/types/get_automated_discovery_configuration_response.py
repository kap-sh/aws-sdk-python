"""Generated from Smithy shape ``com.amazonaws.macie2#GetAutomatedDiscoveryConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_macie2.types.auto_enable_mode
    import aws_sdk_macie2.types.automated_discovery_status
    import aws_sdk_macie2.types.classification_scope_id
    import aws_sdk_macie2.types.sensitivity_inspection_template_id
    import aws_sdk_macie2.types.timestamp


class GetAutomatedDiscoveryConfigurationResponse(TypedDict):
    auto_enable_organization_members: NotRequired[
        "aws_sdk_macie2.types.auto_enable_mode.AutoEnableMode"
    ]
    """<p>Specifies whether automated sensitive data discovery is enabled automatically for accounts in the organization. Possible values are: ALL, enable it for all existing accounts and new member accounts; NEW, enable it only for new member accounts; and, NONE, don't enable it for any accounts.</p>"""
    classification_scope_id: NotRequired[
        "aws_sdk_macie2.types.classification_scope_id.ClassificationScopeId"
    ]
    """<p>The unique identifier for the classification scope that's used when performing automated sensitive data discovery. The classification scope specifies S3 buckets to exclude from analyses.</p>"""
    disabled_at: NotRequired["aws_sdk_macie2.types.timestamp.Timestamp"]
    """<p>The date and time, in UTC and extended ISO 8601 format, when automated sensitive data discovery was most recently disabled. This value is null if automated sensitive data discovery is currently enabled.</p>"""
    first_enabled_at: NotRequired["aws_sdk_macie2.types.timestamp.Timestamp"]
    """<p>The date and time, in UTC and extended ISO 8601 format, when automated sensitive data discovery was initially enabled. This value is null if automated sensitive data discovery has never been enabled.</p>"""
    last_updated_at: NotRequired["aws_sdk_macie2.types.timestamp.Timestamp"]
    """<p>The date and time, in UTC and extended ISO 8601 format, when the configuration settings or status of automated sensitive data discovery was most recently changed.</p>"""
    sensitivity_inspection_template_id: NotRequired[
        "aws_sdk_macie2.types.sensitivity_inspection_template_id.SensitivityInspectionTemplateId"
    ]
    """<p>The unique identifier for the sensitivity inspection template that's used when performing automated sensitive data discovery. The template specifies which allow lists, custom data identifiers, and managed data identifiers to use when analyzing data.</p>"""
    status: NotRequired[
        "aws_sdk_macie2.types.automated_discovery_status.AutomatedDiscoveryStatus"
    ]
    """<p>The current status of automated sensitive data discovery for the organization or account. Possible values are: ENABLED, use the specified settings to perform automated sensitive data discovery activities; and, DISABLED, don't perform automated sensitive data discovery activities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAutomatedDiscoveryConfigurationResponse) -> dict:
    out: dict = {}
    if "auto_enable_organization_members" in value:
        import aws_sdk_macie2.types.auto_enable_mode

        out["autoEnableOrganizationMembers"] = (
            aws_sdk_macie2.types.auto_enable_mode.serialize_json(
                value["auto_enable_organization_members"]
            )
        )
    if "classification_scope_id" in value:
        out["classificationScopeId"] = value["classification_scope_id"]
    if "disabled_at" in value:
        import aws_sdk_macie2.types.timestamp

        out["disabledAt"] = aws_sdk_macie2.types.timestamp.serialize_json(
            value["disabled_at"]
        )
    if "first_enabled_at" in value:
        import aws_sdk_macie2.types.timestamp

        out["firstEnabledAt"] = aws_sdk_macie2.types.timestamp.serialize_json(
            value["first_enabled_at"]
        )
    if "last_updated_at" in value:
        import aws_sdk_macie2.types.timestamp

        out["lastUpdatedAt"] = aws_sdk_macie2.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "sensitivity_inspection_template_id" in value:
        out["sensitivityInspectionTemplateId"] = value[
            "sensitivity_inspection_template_id"
        ]
    if "status" in value:
        import aws_sdk_macie2.types.automated_discovery_status

        out["status"] = aws_sdk_macie2.types.automated_discovery_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> GetAutomatedDiscoveryConfigurationResponse:
    out: GetAutomatedDiscoveryConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "autoEnableOrganizationMembers" in data:
        import aws_sdk_macie2.types.auto_enable_mode

        out["auto_enable_organization_members"] = (
            aws_sdk_macie2.types.auto_enable_mode.deserialize_json(
                data["autoEnableOrganizationMembers"]
            )
        )
    if "classificationScopeId" in data:
        out["classification_scope_id"] = data["classificationScopeId"]
    if "disabledAt" in data:
        import aws_sdk_macie2.types.timestamp

        out["disabled_at"] = aws_sdk_macie2.types.timestamp.deserialize_json(
            data["disabledAt"]
        )
    if "firstEnabledAt" in data:
        import aws_sdk_macie2.types.timestamp

        out["first_enabled_at"] = aws_sdk_macie2.types.timestamp.deserialize_json(
            data["firstEnabledAt"]
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_macie2.types.timestamp

        out["last_updated_at"] = aws_sdk_macie2.types.timestamp.deserialize_json(
            data["lastUpdatedAt"]
        )
    if "sensitivityInspectionTemplateId" in data:
        out["sensitivity_inspection_template_id"] = data[
            "sensitivityInspectionTemplateId"
        ]
    if "status" in data:
        import aws_sdk_macie2.types.automated_discovery_status

        out["status"] = (
            aws_sdk_macie2.types.automated_discovery_status.deserialize_json(
                data["status"]
            )
        )
    return out
