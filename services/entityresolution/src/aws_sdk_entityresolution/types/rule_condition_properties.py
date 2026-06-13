"""Generated from Smithy shape ``com.amazonaws.entityresolution#RuleConditionProperties``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_entityresolution.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_entityresolution.types.matching_config
    import aws_sdk_entityresolution.types.rule_condition_list


class RuleConditionProperties(TypedDict):
    rules: "aws_sdk_entityresolution.types.rule_condition_list.RuleConditionList"
    """<p> A list of rule objects, each of which have fields <code>ruleName</code> and <code>condition</code>. </p>"""
    matching_config: NotRequired[
        "aws_sdk_entityresolution.types.matching_config.MatchingConfig"
    ]
    """<p>An object that contains configuration settings for the matching process.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleConditionProperties) -> dict:
    out: dict = {}
    import aws_sdk_entityresolution.types.rule_condition_list

    out["rules"] = aws_sdk_entityresolution.types.rule_condition_list.serialize_json(
        value["rules"]
    )
    if "matching_config" in value:
        import aws_sdk_entityresolution.types.matching_config

        out["matchingConfig"] = (
            aws_sdk_entityresolution.types.matching_config.serialize_json(
                value["matching_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> RuleConditionProperties:
    out: RuleConditionProperties = {}  # type: ignore[typeddict-item]
    if "rules" in data:
        import aws_sdk_entityresolution.types.rule_condition_list

        out["rules"] = (
            aws_sdk_entityresolution.types.rule_condition_list.deserialize_json(
                data["rules"]
            )
        )
    else:
        raise DeserializationError("RuleConditionProperties.rules required")
    if "matchingConfig" in data:
        import aws_sdk_entityresolution.types.matching_config

        out["matching_config"] = (
            aws_sdk_entityresolution.types.matching_config.deserialize_json(
                data["matchingConfig"]
            )
        )
    return out
