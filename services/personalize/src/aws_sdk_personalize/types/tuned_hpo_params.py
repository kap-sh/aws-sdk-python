"""Generated from Smithy shape ``com.amazonaws.personalize#TunedHPOParams``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize.types.hyper_parameters


class TunedHPOParams(TypedDict, closed=True):
    algorithm_hyper_parameters: NotRequired[
        "aws_sdk_personalize.types.hyper_parameters.HyperParameters"
    ]
    """<p>A list of the hyperparameter values of the best performing model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TunedHPOParams) -> dict:
    out: dict = {}
    if "algorithm_hyper_parameters" in value:
        import aws_sdk_personalize.types.hyper_parameters

        out["algorithmHyperParameters"] = (
            aws_sdk_personalize.types.hyper_parameters.serialize_aws_json_1_1(
                value["algorithm_hyper_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TunedHPOParams:
    out: TunedHPOParams = {}  # type: ignore[typeddict-item]
    if "algorithmHyperParameters" in data:
        import aws_sdk_personalize.types.hyper_parameters

        out["algorithm_hyper_parameters"] = (
            aws_sdk_personalize.types.hyper_parameters.deserialize_aws_json_1_1(
                data["algorithmHyperParameters"]
            )
        )
    return out
