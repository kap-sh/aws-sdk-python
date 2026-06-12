"""Generated from Smithy shape ``com.amazonaws.computeoptimizer#EBSSavingsEstimationMode``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_compute_optimizer.types.ebs_savings_estimation_mode_source


class EBSSavingsEstimationMode(TypedDict):
    source: NotRequired[
        "aws_sdk_compute_optimizer.types.ebs_savings_estimation_mode_source.EBSSavingsEstimationModeSource"
    ]
    """<p> Describes the source for calculating the savings opportunity for Amazon EBS volumes. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EBSSavingsEstimationMode) -> dict:
    out: dict = {}
    if "source" in value:
        import aws_sdk_compute_optimizer.types.ebs_savings_estimation_mode_source

        out["source"] = (
            aws_sdk_compute_optimizer.types.ebs_savings_estimation_mode_source.serialize_aws_json_1_0(
                value["source"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EBSSavingsEstimationMode:
    out: EBSSavingsEstimationMode = {}  # type: ignore[typeddict-item]
    if "source" in data:
        import aws_sdk_compute_optimizer.types.ebs_savings_estimation_mode_source

        out["source"] = (
            aws_sdk_compute_optimizer.types.ebs_savings_estimation_mode_source.deserialize_aws_json_1_0(
                data["source"]
            )
        )
    return out
