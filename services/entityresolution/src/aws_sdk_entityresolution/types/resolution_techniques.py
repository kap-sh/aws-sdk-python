"""Generated from Smithy shape ``com.amazonaws.entityresolution#ResolutionTechniques``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.provider_properties
    import aws_sdk_entityresolution.types.resolution_type
    import aws_sdk_entityresolution.types.rule_based_properties
    import aws_sdk_entityresolution.types.rule_condition_properties


class ResolutionTechniques(TypedDict, closed=True):
    resolution_type: "aws_sdk_entityresolution.types.resolution_type.ResolutionType"
    """<p>The type of matching workflow to create. Specify one of the following types: </p> <ul> <li> <p> <code>RULE_MATCHING</code>: Match records using configurable rule-based criteria </p> </li> <li> <p> <code>ML_MATCHING</code>: Match records using machine learning models </p> </li> <li> <p> <code>PROVIDER</code>: Match records using a third-party matching provider</p> </li> </ul>"""
    rule_based_properties: NotRequired[
        "aws_sdk_entityresolution.types.rule_based_properties.RuleBasedProperties"
    ]
    """<p>An object which defines the list of matching rules to run and has a field <code>rules</code>, which is a list of rule objects.</p>"""
    rule_condition_properties: NotRequired[
        "aws_sdk_entityresolution.types.rule_condition_properties.RuleConditionProperties"
    ]
    """<p>An object containing the <code>rules</code> for a matching workflow.</p>"""
    provider_properties: NotRequired[
        "aws_sdk_entityresolution.types.provider_properties.ProviderProperties"
    ]
    """<p>The properties of the provider service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResolutionTechniques) -> dict:
    out: dict = {}
    import aws_sdk_entityresolution.types.resolution_type

    out["resolutionType"] = (
        aws_sdk_entityresolution.types.resolution_type.serialize_json(
            value["resolution_type"]
        )
    )
    if "rule_based_properties" in value:
        import aws_sdk_entityresolution.types.rule_based_properties

        out["ruleBasedProperties"] = (
            aws_sdk_entityresolution.types.rule_based_properties.serialize_json(
                value["rule_based_properties"]
            )
        )
    if "rule_condition_properties" in value:
        import aws_sdk_entityresolution.types.rule_condition_properties

        out["ruleConditionProperties"] = (
            aws_sdk_entityresolution.types.rule_condition_properties.serialize_json(
                value["rule_condition_properties"]
            )
        )
    if "provider_properties" in value:
        import aws_sdk_entityresolution.types.provider_properties

        out["providerProperties"] = (
            aws_sdk_entityresolution.types.provider_properties.serialize_json(
                value["provider_properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ResolutionTechniques:
    out: ResolutionTechniques = {}  # type: ignore[typeddict-item]
    if "resolutionType" in data:
        import aws_sdk_entityresolution.types.resolution_type

        out["resolution_type"] = (
            aws_sdk_entityresolution.types.resolution_type.deserialize_json(
                data["resolutionType"]
            )
        )
    else:
        raise DeserializationError("ResolutionTechniques.resolution_type required")
    if "ruleBasedProperties" in data:
        import aws_sdk_entityresolution.types.rule_based_properties

        out["rule_based_properties"] = (
            aws_sdk_entityresolution.types.rule_based_properties.deserialize_json(
                data["ruleBasedProperties"]
            )
        )
    if "ruleConditionProperties" in data:
        import aws_sdk_entityresolution.types.rule_condition_properties

        out["rule_condition_properties"] = (
            aws_sdk_entityresolution.types.rule_condition_properties.deserialize_json(
                data["ruleConditionProperties"]
            )
        )
    if "providerProperties" in data:
        import aws_sdk_entityresolution.types.provider_properties

        out["provider_properties"] = (
            aws_sdk_entityresolution.types.provider_properties.deserialize_json(
                data["providerProperties"]
            )
        )
    return out
