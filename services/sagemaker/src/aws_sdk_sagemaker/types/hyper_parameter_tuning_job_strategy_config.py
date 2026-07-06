"""Generated from Smithy shape ``com.amazonaws.sagemaker#HyperParameterTuningJobStrategyConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.hyperband_strategy_config


class HyperParameterTuningJobStrategyConfig(TypedDict, closed=True):
    hyperband_strategy_config: NotRequired[
        "aws_sdk_sagemaker.types.hyperband_strategy_config.HyperbandStrategyConfig"
    ]
    """<p>The configuration for the object that specifies the <code>Hyperband</code> strategy. This parameter is only supported for the <code>Hyperband</code> selection for <code>Strategy</code> within the <code>HyperParameterTuningJobConfig</code> API.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobStrategyConfig) -> dict:
    out: dict = {}
    if "hyperband_strategy_config" in value:
        import aws_sdk_sagemaker.types.hyperband_strategy_config

        out["HyperbandStrategyConfig"] = (
            aws_sdk_sagemaker.types.hyperband_strategy_config.serialize_aws_json_1_1(
                value["hyperband_strategy_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterTuningJobStrategyConfig:
    out: HyperParameterTuningJobStrategyConfig = {}  # type: ignore[typeddict-item]
    if "HyperbandStrategyConfig" in data:
        import aws_sdk_sagemaker.types.hyperband_strategy_config

        out["hyperband_strategy_config"] = (
            aws_sdk_sagemaker.types.hyperband_strategy_config.deserialize_aws_json_1_1(
                data["HyperbandStrategyConfig"]
            )
        )
    return out
