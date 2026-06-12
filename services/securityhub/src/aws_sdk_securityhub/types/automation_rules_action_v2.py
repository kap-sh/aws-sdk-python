"""Generated from Smithy shape ``com.amazonaws.securityhub#AutomationRulesActionV2``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.automation_rules_action_type_v2
    import aws_sdk_securityhub.types.automation_rules_finding_fields_update_v2
    import aws_sdk_securityhub.types.external_integration_configuration


class AutomationRulesActionV2(TypedDict):
    type: NotRequired[
        "aws_sdk_securityhub.types.automation_rules_action_type_v2.AutomationRulesActionTypeV2"
    ]
    """<p>The category of action to be executed by the automation rule.</p>"""
    finding_fields_update: NotRequired[
        "aws_sdk_securityhub.types.automation_rules_finding_fields_update_v2.AutomationRulesFindingFieldsUpdateV2"
    ]
    """<p>The changes to be applied to fields in a security finding when an automation rule is triggered.</p>"""
    external_integration_configuration: NotRequired[
        "aws_sdk_securityhub.types.external_integration_configuration.ExternalIntegrationConfiguration"
    ]
    """<p>The settings for integrating automation rule actions with external systems or service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomationRulesActionV2) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_securityhub.types.automation_rules_action_type_v2

        out["Type"] = (
            aws_sdk_securityhub.types.automation_rules_action_type_v2.serialize_json(
                value["type"]
            )
        )
    if "finding_fields_update" in value:
        import aws_sdk_securityhub.types.automation_rules_finding_fields_update_v2

        out["FindingFieldsUpdate"] = (
            aws_sdk_securityhub.types.automation_rules_finding_fields_update_v2.serialize_json(
                value["finding_fields_update"]
            )
        )
    if "external_integration_configuration" in value:
        import aws_sdk_securityhub.types.external_integration_configuration

        out["ExternalIntegrationConfiguration"] = (
            aws_sdk_securityhub.types.external_integration_configuration.serialize_json(
                value["external_integration_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomationRulesActionV2:
    out: AutomationRulesActionV2 = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_securityhub.types.automation_rules_action_type_v2

        out["type"] = (
            aws_sdk_securityhub.types.automation_rules_action_type_v2.deserialize_json(
                data["Type"]
            )
        )
    if "FindingFieldsUpdate" in data:
        import aws_sdk_securityhub.types.automation_rules_finding_fields_update_v2

        out["finding_fields_update"] = (
            aws_sdk_securityhub.types.automation_rules_finding_fields_update_v2.deserialize_json(
                data["FindingFieldsUpdate"]
            )
        )
    if "ExternalIntegrationConfiguration" in data:
        import aws_sdk_securityhub.types.external_integration_configuration

        out["external_integration_configuration"] = (
            aws_sdk_securityhub.types.external_integration_configuration.deserialize_json(
                data["ExternalIntegrationConfiguration"]
            )
        )
    return out
