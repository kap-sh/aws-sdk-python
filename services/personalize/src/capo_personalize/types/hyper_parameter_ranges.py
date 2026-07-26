"""Generated from Smithy shape ``com.amazonaws.personalize#HyperParameterRanges``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.categorical_hyper_parameter_ranges
    import capo_personalize.types.continuous_hyper_parameter_ranges
    import capo_personalize.types.integer_hyper_parameter_ranges


class HyperParameterRanges(TypedDict, closed=True):
    integer_hyper_parameter_ranges: NotRequired[
        "capo_personalize.types.integer_hyper_parameter_ranges.IntegerHyperParameterRanges"
    ]
    """<p>The integer-valued hyperparameters and their ranges.</p>"""
    continuous_hyper_parameter_ranges: NotRequired[
        "capo_personalize.types.continuous_hyper_parameter_ranges.ContinuousHyperParameterRanges"
    ]
    """<p>The continuous hyperparameters and their ranges.</p>"""
    categorical_hyper_parameter_ranges: NotRequired[
        "capo_personalize.types.categorical_hyper_parameter_ranges.CategoricalHyperParameterRanges"
    ]
    """<p>The categorical hyperparameters and their ranges.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterRanges) -> dict:
    out: dict = {}
    if "integer_hyper_parameter_ranges" in value:
        import capo_personalize.types.integer_hyper_parameter_ranges

        out["integerHyperParameterRanges"] = (
            capo_personalize.types.integer_hyper_parameter_ranges.serialize_aws_json_1_1(
                value["integer_hyper_parameter_ranges"]
            )
        )
    if "continuous_hyper_parameter_ranges" in value:
        import capo_personalize.types.continuous_hyper_parameter_ranges

        out["continuousHyperParameterRanges"] = (
            capo_personalize.types.continuous_hyper_parameter_ranges.serialize_aws_json_1_1(
                value["continuous_hyper_parameter_ranges"]
            )
        )
    if "categorical_hyper_parameter_ranges" in value:
        import capo_personalize.types.categorical_hyper_parameter_ranges

        out["categoricalHyperParameterRanges"] = (
            capo_personalize.types.categorical_hyper_parameter_ranges.serialize_aws_json_1_1(
                value["categorical_hyper_parameter_ranges"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterRanges:
    out: HyperParameterRanges = {}  # type: ignore[typeddict-item]
    if "integerHyperParameterRanges" in data:
        import capo_personalize.types.integer_hyper_parameter_ranges

        out["integer_hyper_parameter_ranges"] = (
            capo_personalize.types.integer_hyper_parameter_ranges.deserialize_aws_json_1_1(
                data["integerHyperParameterRanges"]
            )
        )
    if "continuousHyperParameterRanges" in data:
        import capo_personalize.types.continuous_hyper_parameter_ranges

        out["continuous_hyper_parameter_ranges"] = (
            capo_personalize.types.continuous_hyper_parameter_ranges.deserialize_aws_json_1_1(
                data["continuousHyperParameterRanges"]
            )
        )
    if "categoricalHyperParameterRanges" in data:
        import capo_personalize.types.categorical_hyper_parameter_ranges

        out["categorical_hyper_parameter_ranges"] = (
            capo_personalize.types.categorical_hyper_parameter_ranges.deserialize_aws_json_1_1(
                data["categoricalHyperParameterRanges"]
            )
        )
    return out
