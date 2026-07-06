"""Generated from Smithy shape ``com.amazonaws.sagemaker#DriftCheckBias``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.file_source
    import aws_sdk_sagemaker.types.metrics_source


class DriftCheckBias(TypedDict, closed=True):
    config_file: NotRequired["aws_sdk_sagemaker.types.file_source.FileSource"]
    """<p>The bias config file for a model.</p>"""
    pre_training_constraints: NotRequired[
        "aws_sdk_sagemaker.types.metrics_source.MetricsSource"
    ]
    """<p>The pre-training constraints.</p>"""
    post_training_constraints: NotRequired[
        "aws_sdk_sagemaker.types.metrics_source.MetricsSource"
    ]
    """<p>The post-training constraints.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DriftCheckBias) -> dict:
    out: dict = {}
    if "config_file" in value:
        import aws_sdk_sagemaker.types.file_source

        out["ConfigFile"] = aws_sdk_sagemaker.types.file_source.serialize_aws_json_1_1(
            value["config_file"]
        )
    if "pre_training_constraints" in value:
        import aws_sdk_sagemaker.types.metrics_source

        out["PreTrainingConstraints"] = (
            aws_sdk_sagemaker.types.metrics_source.serialize_aws_json_1_1(
                value["pre_training_constraints"]
            )
        )
    if "post_training_constraints" in value:
        import aws_sdk_sagemaker.types.metrics_source

        out["PostTrainingConstraints"] = (
            aws_sdk_sagemaker.types.metrics_source.serialize_aws_json_1_1(
                value["post_training_constraints"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DriftCheckBias:
    out: DriftCheckBias = {}  # type: ignore[typeddict-item]
    if "ConfigFile" in data:
        import aws_sdk_sagemaker.types.file_source

        out["config_file"] = (
            aws_sdk_sagemaker.types.file_source.deserialize_aws_json_1_1(
                data["ConfigFile"]
            )
        )
    if "PreTrainingConstraints" in data:
        import aws_sdk_sagemaker.types.metrics_source

        out["pre_training_constraints"] = (
            aws_sdk_sagemaker.types.metrics_source.deserialize_aws_json_1_1(
                data["PreTrainingConstraints"]
            )
        )
    if "PostTrainingConstraints" in data:
        import aws_sdk_sagemaker.types.metrics_source

        out["post_training_constraints"] = (
            aws_sdk_sagemaker.types.metrics_source.deserialize_aws_json_1_1(
                data["PostTrainingConstraints"]
            )
        )
    return out
