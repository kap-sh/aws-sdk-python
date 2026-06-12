"""Generated from Smithy shape ``com.amazonaws.forecast#HyperParameterTuningJobConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_forecast.types.parameter_ranges


class HyperParameterTuningJobConfig(TypedDict):
    parameter_ranges: NotRequired[
        "aws_sdk_forecast.types.parameter_ranges.ParameterRanges"
    ]
    """<p>Specifies the ranges of valid values for the hyperparameters.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HyperParameterTuningJobConfig) -> dict:
    out: dict = {}
    if "parameter_ranges" in value:
        import aws_sdk_forecast.types.parameter_ranges

        out["ParameterRanges"] = (
            aws_sdk_forecast.types.parameter_ranges.serialize_aws_json_1_1(
                value["parameter_ranges"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> HyperParameterTuningJobConfig:
    out: HyperParameterTuningJobConfig = {}  # type: ignore[typeddict-item]
    if "ParameterRanges" in data:
        import aws_sdk_forecast.types.parameter_ranges

        out["parameter_ranges"] = (
            aws_sdk_forecast.types.parameter_ranges.deserialize_aws_json_1_1(
                data["ParameterRanges"]
            )
        )
    return out
