"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleVerdictToEvaluate``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_mailmanager.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_mailmanager.types.analysis
    import capo_mailmanager.types.rule_verdict_attribute


class _RuleVerdictToEvaluate_Attribute(TypedDict, closed=True):
    Attribute: "capo_mailmanager.types.rule_verdict_attribute.RuleVerdictAttribute"


class _RuleVerdictToEvaluate_Analysis(TypedDict, closed=True):
    Analysis: "capo_mailmanager.types.analysis.Analysis"


RuleVerdictToEvaluate: TypeAlias = (
    _RuleVerdictToEvaluate_Attribute | _RuleVerdictToEvaluate_Analysis
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleVerdictToEvaluate) -> dict:
    if "Attribute" in value:
        import capo_mailmanager.types.rule_verdict_attribute

        return {
            "Attribute": capo_mailmanager.types.rule_verdict_attribute.serialize_aws_json_1_0(
                value["Attribute"]
            )
        }
    elif "Analysis" in value:
        import capo_mailmanager.types.analysis

        return {
            "Analysis": capo_mailmanager.types.analysis.serialize_aws_json_1_0(
                value["Analysis"]
            )
        }
    else:
        raise SerializationError("RuleVerdictToEvaluate: no variant present")


def deserialize_aws_json_1_0(data: dict) -> RuleVerdictToEvaluate:
    if "Attribute" in data:
        import capo_mailmanager.types.rule_verdict_attribute

        return {
            "Attribute": capo_mailmanager.types.rule_verdict_attribute.deserialize_aws_json_1_0(
                data["Attribute"]
            )
        }
    elif "Analysis" in data:
        import capo_mailmanager.types.analysis

        return {
            "Analysis": capo_mailmanager.types.analysis.deserialize_aws_json_1_0(
                data["Analysis"]
            )
        }
    else:
        raise DeserializationError("RuleVerdictToEvaluate: no recognized variant key")
