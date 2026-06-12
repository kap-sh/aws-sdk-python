"""Generated from Smithy shape ``com.amazonaws.sagemaker#ModelQuality``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.metrics_source


class ModelQuality(TypedDict):
    statistics: NotRequired["aws_sdk_sagemaker.types.metrics_source.MetricsSource"]
    """<p>Model quality statistics.</p>"""
    constraints: NotRequired["aws_sdk_sagemaker.types.metrics_source.MetricsSource"]
    """<p>Model quality constraints.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ModelQuality) -> dict:
    out: dict = {}
    if "statistics" in value:
        import aws_sdk_sagemaker.types.metrics_source

        out["Statistics"] = (
            aws_sdk_sagemaker.types.metrics_source.serialize_aws_json_1_1(
                value["statistics"]
            )
        )
    if "constraints" in value:
        import aws_sdk_sagemaker.types.metrics_source

        out["Constraints"] = (
            aws_sdk_sagemaker.types.metrics_source.serialize_aws_json_1_1(
                value["constraints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ModelQuality:
    out: ModelQuality = {}  # type: ignore[typeddict-item]
    if "Statistics" in data:
        import aws_sdk_sagemaker.types.metrics_source

        out["statistics"] = (
            aws_sdk_sagemaker.types.metrics_source.deserialize_aws_json_1_1(
                data["Statistics"]
            )
        )
    if "Constraints" in data:
        import aws_sdk_sagemaker.types.metrics_source

        out["constraints"] = (
            aws_sdk_sagemaker.types.metrics_source.deserialize_aws_json_1_1(
                data["Constraints"]
            )
        )
    return out
