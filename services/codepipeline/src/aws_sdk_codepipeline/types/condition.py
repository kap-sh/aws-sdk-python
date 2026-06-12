"""Generated from Smithy shape ``com.amazonaws.codepipeline#Condition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codepipeline.types.result
    import aws_sdk_codepipeline.types.rule_declaration_list


class Condition(TypedDict):
    result: NotRequired["aws_sdk_codepipeline.types.result.Result"]
    """<p>The action to be done when the condition is met. For example, rolling back an execution for a failure condition.</p>"""
    rules: NotRequired[
        "aws_sdk_codepipeline.types.rule_declaration_list.RuleDeclarationList"
    ]
    """<p>The rules that make up the condition.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Condition) -> dict:
    out: dict = {}
    if "result" in value:
        import aws_sdk_codepipeline.types.result

        out["result"] = aws_sdk_codepipeline.types.result.serialize_aws_json_1_1(
            value["result"]
        )
    if "rules" in value:
        import aws_sdk_codepipeline.types.rule_declaration_list

        out["rules"] = (
            aws_sdk_codepipeline.types.rule_declaration_list.serialize_aws_json_1_1(
                value["rules"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Condition:
    out: Condition = {}  # type: ignore[typeddict-item]
    if "result" in data:
        import aws_sdk_codepipeline.types.result

        out["result"] = aws_sdk_codepipeline.types.result.deserialize_aws_json_1_1(
            data["result"]
        )
    if "rules" in data:
        import aws_sdk_codepipeline.types.rule_declaration_list

        out["rules"] = (
            aws_sdk_codepipeline.types.rule_declaration_list.deserialize_aws_json_1_1(
                data["rules"]
            )
        )
    return out
