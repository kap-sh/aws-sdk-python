"""Generated from Smithy shape ``com.amazonaws.sagemaker#DriftCheckExplainability``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.file_source
    import capo_sagemaker.types.metrics_source


class DriftCheckExplainability(TypedDict, closed=True):
    constraints: NotRequired["capo_sagemaker.types.metrics_source.MetricsSource"]
    """<p>The drift check explainability constraints.</p>"""
    config_file: NotRequired["capo_sagemaker.types.file_source.FileSource"]
    """<p>The explainability config file for the model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DriftCheckExplainability) -> dict:
    out: dict = {}
    if "constraints" in value:
        import capo_sagemaker.types.metrics_source

        out["Constraints"] = capo_sagemaker.types.metrics_source.serialize_aws_json_1_1(
            value["constraints"]
        )
    if "config_file" in value:
        import capo_sagemaker.types.file_source

        out["ConfigFile"] = capo_sagemaker.types.file_source.serialize_aws_json_1_1(
            value["config_file"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DriftCheckExplainability:
    out: DriftCheckExplainability = {}  # type: ignore[typeddict-item]
    if "Constraints" in data:
        import capo_sagemaker.types.metrics_source

        out["constraints"] = (
            capo_sagemaker.types.metrics_source.deserialize_aws_json_1_1(
                data["Constraints"]
            )
        )
    if "ConfigFile" in data:
        import capo_sagemaker.types.file_source

        out["config_file"] = capo_sagemaker.types.file_source.deserialize_aws_json_1_1(
            data["ConfigFile"]
        )
    return out
