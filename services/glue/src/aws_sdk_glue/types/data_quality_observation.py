"""Generated from Smithy shape ``com.amazonaws.glue#DataQualityObservation``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.data_quality_observation_description
    import aws_sdk_glue.types.metric_based_observation


class DataQualityObservation(TypedDict):
    description: NotRequired[
        "aws_sdk_glue.types.data_quality_observation_description.DataQualityObservationDescription"
    ]
    """<p>A description of the data quality observation.</p>"""
    metric_based_observation: NotRequired[
        "aws_sdk_glue.types.metric_based_observation.MetricBasedObservation"
    ]
    """<p>An object of type <code>MetricBasedObservation</code> representing the observation that is based on evaluated data quality metrics.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataQualityObservation) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "metric_based_observation" in value:
        import aws_sdk_glue.types.metric_based_observation

        out["MetricBasedObservation"] = (
            aws_sdk_glue.types.metric_based_observation.serialize_aws_json_1_1(
                value["metric_based_observation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataQualityObservation:
    out: DataQualityObservation = {}  # type: ignore[typeddict-item]
    if "Description" in data:
        out["description"] = data["Description"]
    if "MetricBasedObservation" in data:
        import aws_sdk_glue.types.metric_based_observation

        out["metric_based_observation"] = (
            aws_sdk_glue.types.metric_based_observation.deserialize_aws_json_1_1(
                data["MetricBasedObservation"]
            )
        )
    return out
