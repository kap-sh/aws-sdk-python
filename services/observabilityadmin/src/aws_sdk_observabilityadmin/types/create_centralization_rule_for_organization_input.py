"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#CreateCentralizationRuleForOrganizationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_observabilityadmin.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.centralization_rule
    import aws_sdk_observabilityadmin.types.rule_name
    import aws_sdk_observabilityadmin.types.tag_map_input


class CreateCentralizationRuleForOrganizationInput(TypedDict, closed=True):
    rule_name: "aws_sdk_observabilityadmin.types.rule_name.RuleName"
    """<p>A unique name for the organization-wide centralization rule being created.</p>"""
    rule: "aws_sdk_observabilityadmin.types.centralization_rule.CentralizationRule"
    """<p>The configuration details for the organization-wide centralization rule, including the source configuration and the destination configuration to centralize telemetry data across the organization.</p>"""
    tags: NotRequired["aws_sdk_observabilityadmin.types.tag_map_input.TagMapInput"]
    """<p>The key-value pairs to associate with the organization telemetry rule resource for categorization and management purposes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCentralizationRuleForOrganizationInput) -> dict:
    out: dict = {}
    out["RuleName"] = value["rule_name"]
    import aws_sdk_observabilityadmin.types.centralization_rule

    out["Rule"] = aws_sdk_observabilityadmin.types.centralization_rule.serialize_json(
        value["rule"]
    )
    if "tags" in value:
        import aws_sdk_observabilityadmin.types.tag_map_input

        out["Tags"] = aws_sdk_observabilityadmin.types.tag_map_input.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateCentralizationRuleForOrganizationInput:
    out: CreateCentralizationRuleForOrganizationInput = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    else:
        raise DeserializationError(
            "CreateCentralizationRuleForOrganizationInput.rule_name required"
        )
    if "Rule" in data:
        import aws_sdk_observabilityadmin.types.centralization_rule

        out["rule"] = (
            aws_sdk_observabilityadmin.types.centralization_rule.deserialize_json(
                data["Rule"]
            )
        )
    else:
        raise DeserializationError(
            "CreateCentralizationRuleForOrganizationInput.rule required"
        )
    if "Tags" in data:
        import aws_sdk_observabilityadmin.types.tag_map_input

        out["tags"] = aws_sdk_observabilityadmin.types.tag_map_input.deserialize_json(
            data["Tags"]
        )
    return out
