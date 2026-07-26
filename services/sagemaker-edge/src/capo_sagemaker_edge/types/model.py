"""Generated from Smithy shape ``com.amazonaws.sagemakeredge#Model``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_edge.types.edge_metrics
    import capo_sagemaker_edge.types.model_name
    import capo_sagemaker_edge.types.timestamp
    import capo_sagemaker_edge.types.version


class Model(TypedDict, closed=True):
    model_name: NotRequired["capo_sagemaker_edge.types.model_name.ModelName"]
    """<p>The name of the model.</p>"""
    model_version: NotRequired["capo_sagemaker_edge.types.version.Version"]
    """<p>The version of the model.</p>"""
    latest_sample_time: NotRequired["capo_sagemaker_edge.types.timestamp.Timestamp"]
    """<p>The timestamp of the last data sample taken.</p>"""
    latest_inference: NotRequired["capo_sagemaker_edge.types.timestamp.Timestamp"]
    """<p>The timestamp of the last inference that was made.</p>"""
    model_metrics: NotRequired["capo_sagemaker_edge.types.edge_metrics.EdgeMetrics"]
    """<p>Information required for model metrics.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Model) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "model_version" in value:
        out["ModelVersion"] = value["model_version"]
    if "latest_sample_time" in value:
        import capo_sagemaker_edge.types.timestamp

        out["LatestSampleTime"] = capo_sagemaker_edge.types.timestamp.serialize_json(
            value["latest_sample_time"]
        )
    if "latest_inference" in value:
        import capo_sagemaker_edge.types.timestamp

        out["LatestInference"] = capo_sagemaker_edge.types.timestamp.serialize_json(
            value["latest_inference"]
        )
    if "model_metrics" in value:
        import capo_sagemaker_edge.types.edge_metrics

        out["ModelMetrics"] = capo_sagemaker_edge.types.edge_metrics.serialize_json(
            value["model_metrics"]
        )
    return out


def deserialize_json(data: dict) -> Model:
    out: Model = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    if "LatestSampleTime" in data:
        import capo_sagemaker_edge.types.timestamp

        out["latest_sample_time"] = (
            capo_sagemaker_edge.types.timestamp.deserialize_json(
                data["LatestSampleTime"]
            )
        )
    if "LatestInference" in data:
        import capo_sagemaker_edge.types.timestamp

        out["latest_inference"] = capo_sagemaker_edge.types.timestamp.deserialize_json(
            data["LatestInference"]
        )
    if "ModelMetrics" in data:
        import capo_sagemaker_edge.types.edge_metrics

        out["model_metrics"] = capo_sagemaker_edge.types.edge_metrics.deserialize_json(
            data["ModelMetrics"]
        )
    return out
