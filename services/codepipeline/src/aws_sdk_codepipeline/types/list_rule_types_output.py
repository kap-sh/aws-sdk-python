"""Generated from Smithy shape ``com.amazonaws.codepipeline#ListRuleTypesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.rule_type_list


class ListRuleTypesOutput(TypedDict, closed=True):
    rule_types: "aws_sdk_codepipeline.types.rule_type_list.RuleTypeList"
    """<p>Lists the rules that are configured for the condition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListRuleTypesOutput) -> dict:
    out: dict = {}
    import aws_sdk_codepipeline.types.rule_type_list

    out["ruleTypes"] = aws_sdk_codepipeline.types.rule_type_list.serialize_aws_json_1_1(
        value["rule_types"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListRuleTypesOutput:
    out: ListRuleTypesOutput = {}  # type: ignore[typeddict-item]
    if "ruleTypes" in data:
        import aws_sdk_codepipeline.types.rule_type_list

        out["rule_types"] = (
            aws_sdk_codepipeline.types.rule_type_list.deserialize_aws_json_1_1(
                data["ruleTypes"]
            )
        )
    else:
        raise DeserializationError("ListRuleTypesOutput.rule_types required")
    return out
