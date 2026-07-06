"""Generated from Smithy shape ``com.amazonaws.sagemaker#HumanLoopActivationConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.human_loop_activation_conditions_config


class HumanLoopActivationConfig(TypedDict, closed=True):
    human_loop_activation_conditions_config: NotRequired[
        "aws_sdk_sagemaker.types.human_loop_activation_conditions_config.HumanLoopActivationConditionsConfig"
    ]
    """<p>Container structure for defining under what conditions SageMaker creates a human loop.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HumanLoopActivationConfig) -> dict:
    out: dict = {}
    if "human_loop_activation_conditions_config" in value:
        import aws_sdk_sagemaker.types.human_loop_activation_conditions_config

        out["HumanLoopActivationConditionsConfig"] = (
            aws_sdk_sagemaker.types.human_loop_activation_conditions_config.serialize_aws_json_1_1(
                value["human_loop_activation_conditions_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HumanLoopActivationConfig:
    out: HumanLoopActivationConfig = {}  # type: ignore[typeddict-item]
    if "HumanLoopActivationConditionsConfig" in data:
        import aws_sdk_sagemaker.types.human_loop_activation_conditions_config

        out["human_loop_activation_conditions_config"] = (
            aws_sdk_sagemaker.types.human_loop_activation_conditions_config.deserialize_aws_json_1_1(
                data["HumanLoopActivationConditionsConfig"]
            )
        )
    return out
