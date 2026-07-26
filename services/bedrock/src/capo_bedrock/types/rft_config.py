"""Generated from Smithy shape ``com.amazonaws.bedrock#RFTConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.grader_config
    import capo_bedrock.types.rft_hyper_parameters


class RFTConfig(TypedDict, closed=True):
    grader_config: NotRequired["capo_bedrock.types.grader_config.GraderConfig"]
    """<p> Configuration for the grader that evaluates model responses and provides reward signals during RFT training. </p>"""
    hyper_parameters: NotRequired[
        "capo_bedrock.types.rft_hyper_parameters.RFTHyperParameters"
    ]
    """<p> Hyperparameters that control the reinforcement fine-tuning training process, including learning rate, batch size, and epoch count. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RFTConfig) -> dict:
    out: dict = {}
    if "grader_config" in value:
        import capo_bedrock.types.grader_config

        out["graderConfig"] = capo_bedrock.types.grader_config.serialize_json(
            value["grader_config"]
        )
    if "hyper_parameters" in value:
        import capo_bedrock.types.rft_hyper_parameters

        out["hyperParameters"] = capo_bedrock.types.rft_hyper_parameters.serialize_json(
            value["hyper_parameters"]
        )
    return out


def deserialize_json(data: dict) -> RFTConfig:
    out: RFTConfig = {}  # type: ignore[typeddict-item]
    if "graderConfig" in data:
        import capo_bedrock.types.grader_config

        out["grader_config"] = capo_bedrock.types.grader_config.deserialize_json(
            data["graderConfig"]
        )
    if "hyperParameters" in data:
        import capo_bedrock.types.rft_hyper_parameters

        out["hyper_parameters"] = (
            capo_bedrock.types.rft_hyper_parameters.deserialize_json(
                data["hyperParameters"]
            )
        )
    return out
