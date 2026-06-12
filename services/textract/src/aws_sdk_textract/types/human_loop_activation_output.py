"""Generated from Smithy shape ``com.amazonaws.textract#HumanLoopActivationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_textract.types.human_loop_activation_reasons
    import aws_sdk_textract.types.human_loop_arn
    import aws_sdk_textract.types.synthesized_json_human_loop_activation_conditions_evaluation_results


class HumanLoopActivationOutput(TypedDict):
    human_loop_arn: NotRequired["aws_sdk_textract.types.human_loop_arn.HumanLoopArn"]
    """<p>The Amazon Resource Name (ARN) of the HumanLoop created.</p>"""
    human_loop_activation_reasons: NotRequired[
        "aws_sdk_textract.types.human_loop_activation_reasons.HumanLoopActivationReasons"
    ]
    """<p>Shows if and why human review was needed.</p>"""
    human_loop_activation_conditions_evaluation_results: NotRequired[
        "aws_sdk_textract.types.synthesized_json_human_loop_activation_conditions_evaluation_results.SynthesizedJsonHumanLoopActivationConditionsEvaluationResults"
    ]
    """<p>Shows the result of condition evaluations, including those conditions which activated a human review.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanLoopActivationOutput) -> dict:
    out: dict = {}
    if "human_loop_arn" in value:
        out["HumanLoopArn"] = value["human_loop_arn"]
    if "human_loop_activation_reasons" in value:
        import aws_sdk_textract.types.human_loop_activation_reasons

        out["HumanLoopActivationReasons"] = (
            aws_sdk_textract.types.human_loop_activation_reasons.serialize_aws_json_1_1(
                value["human_loop_activation_reasons"]
            )
        )
    if "human_loop_activation_conditions_evaluation_results" in value:
        out["HumanLoopActivationConditionsEvaluationResults"] = value[
            "human_loop_activation_conditions_evaluation_results"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> HumanLoopActivationOutput:
    out: HumanLoopActivationOutput = {}  # type: ignore[typeddict-item]
    if "HumanLoopArn" in data:
        out["human_loop_arn"] = data["HumanLoopArn"]
    if "HumanLoopActivationReasons" in data:
        import aws_sdk_textract.types.human_loop_activation_reasons

        out["human_loop_activation_reasons"] = (
            aws_sdk_textract.types.human_loop_activation_reasons.deserialize_aws_json_1_1(
                data["HumanLoopActivationReasons"]
            )
        )
    if "HumanLoopActivationConditionsEvaluationResults" in data:
        out["human_loop_activation_conditions_evaluation_results"] = data[
            "HumanLoopActivationConditionsEvaluationResults"
        ]
    return out
