"""Generated from Smithy shape ``com.amazonaws.personalize#HPOConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_personalize.types.hpo_objective
    import aws_sdk_personalize.types.hpo_resource_config
    import aws_sdk_personalize.types.hyper_parameter_ranges


class HPOConfig(TypedDict):
    hpo_objective: NotRequired["aws_sdk_personalize.types.hpo_objective.HPOObjective"]
    """<p>The metric to optimize during HPO.</p> <note> <p>Amazon Personalize doesn't support configuring the <code>hpoObjective</code> at this time.</p> </note>"""
    hpo_resource_config: NotRequired[
        "aws_sdk_personalize.types.hpo_resource_config.HPOResourceConfig"
    ]
    """<p>Describes the resource configuration for HPO.</p>"""
    algorithm_hyper_parameter_ranges: NotRequired[
        "aws_sdk_personalize.types.hyper_parameter_ranges.HyperParameterRanges"
    ]
    """<p>The hyperparameters and their allowable ranges.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HPOConfig) -> dict:
    out: dict = {}
    if "hpo_objective" in value:
        import aws_sdk_personalize.types.hpo_objective

        out["hpoObjective"] = (
            aws_sdk_personalize.types.hpo_objective.serialize_aws_json_1_1(
                value["hpo_objective"]
            )
        )
    if "hpo_resource_config" in value:
        import aws_sdk_personalize.types.hpo_resource_config

        out["hpoResourceConfig"] = (
            aws_sdk_personalize.types.hpo_resource_config.serialize_aws_json_1_1(
                value["hpo_resource_config"]
            )
        )
    if "algorithm_hyper_parameter_ranges" in value:
        import aws_sdk_personalize.types.hyper_parameter_ranges

        out["algorithmHyperParameterRanges"] = (
            aws_sdk_personalize.types.hyper_parameter_ranges.serialize_aws_json_1_1(
                value["algorithm_hyper_parameter_ranges"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HPOConfig:
    out: HPOConfig = {}  # type: ignore[typeddict-item]
    if "hpoObjective" in data:
        import aws_sdk_personalize.types.hpo_objective

        out["hpo_objective"] = (
            aws_sdk_personalize.types.hpo_objective.deserialize_aws_json_1_1(
                data["hpoObjective"]
            )
        )
    if "hpoResourceConfig" in data:
        import aws_sdk_personalize.types.hpo_resource_config

        out["hpo_resource_config"] = (
            aws_sdk_personalize.types.hpo_resource_config.deserialize_aws_json_1_1(
                data["hpoResourceConfig"]
            )
        )
    if "algorithmHyperParameterRanges" in data:
        import aws_sdk_personalize.types.hyper_parameter_ranges

        out["algorithm_hyper_parameter_ranges"] = (
            aws_sdk_personalize.types.hyper_parameter_ranges.deserialize_aws_json_1_1(
                data["algorithmHyperParameterRanges"]
            )
        )
    return out
