"""Generated from Smithy shape ``com.amazonaws.sagemaker#HumanLoopActivationConditionsConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.human_loop_activation_conditions


class HumanLoopActivationConditionsConfig(TypedDict):
    human_loop_activation_conditions: NotRequired[
        "aws_sdk_sagemaker.types.human_loop_activation_conditions.HumanLoopActivationConditions"
    ]
    r"""<p>JSON expressing use-case specific conditions declaratively. If any condition is matched, atomic tasks are created against the configured work team. The set of conditions is different for Rekognition and Textract. For more information about how to structure the JSON, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/a2i-human-fallback-conditions-json-schema.html\">JSON Schema for Human Loop Activation Conditions in Amazon Augmented AI</a> in the <i>Amazon SageMaker Developer Guide</i>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanLoopActivationConditionsConfig) -> dict:
    out: dict = {}
    if "human_loop_activation_conditions" in value:
        out["HumanLoopActivationConditions"] = value["human_loop_activation_conditions"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HumanLoopActivationConditionsConfig:
    out: HumanLoopActivationConditionsConfig = {}  # type: ignore[typeddict-item]
    if "HumanLoopActivationConditions" in data:
        out["human_loop_activation_conditions"] = data["HumanLoopActivationConditions"]
    return out
