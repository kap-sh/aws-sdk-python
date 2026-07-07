"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputationModelConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.computation_model_anomaly_detection_configuration


class ComputationModelConfiguration(TypedDict, closed=True):
    anomaly_detection: NotRequired[
        "aws_sdk_iotsitewise.types.computation_model_anomaly_detection_configuration.ComputationModelAnomalyDetectionConfiguration"
    ]
    """<p>The configuration for the anomaly detection type of computation model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputationModelConfiguration) -> dict:
    out: dict = {}
    if "anomaly_detection" in value:
        import aws_sdk_iotsitewise.types.computation_model_anomaly_detection_configuration

        out["anomalyDetection"] = (
            aws_sdk_iotsitewise.types.computation_model_anomaly_detection_configuration.serialize_json(
                value["anomaly_detection"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComputationModelConfiguration:
    out: ComputationModelConfiguration = {}  # type: ignore[typeddict-item]
    if "anomalyDetection" in data:
        import aws_sdk_iotsitewise.types.computation_model_anomaly_detection_configuration

        out["anomaly_detection"] = (
            aws_sdk_iotsitewise.types.computation_model_anomaly_detection_configuration.deserialize_json(
                data["anomalyDetection"]
            )
        )
    return out
