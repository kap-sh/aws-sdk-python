"""Generated from Smithy shape ``com.amazonaws.frauddetector#TrainingMetricsV2``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.ati_training_metrics_value
    import aws_sdk_frauddetector.types.ofi_training_metrics_value
    import aws_sdk_frauddetector.types.tfi_training_metrics_value


class TrainingMetricsV2(TypedDict, closed=True):
    ofi: NotRequired[
        "aws_sdk_frauddetector.types.ofi_training_metrics_value.OFITrainingMetricsValue"
    ]
    """<p> The Online Fraud Insights (OFI) model training metric details. </p>"""
    tfi: NotRequired[
        "aws_sdk_frauddetector.types.tfi_training_metrics_value.TFITrainingMetricsValue"
    ]
    """<p> The Transaction Fraud Insights (TFI) model training metric details. </p>"""
    ati: NotRequired[
        "aws_sdk_frauddetector.types.ati_training_metrics_value.ATITrainingMetricsValue"
    ]
    """<p> The Account Takeover Insights (ATI) model training metric details. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingMetricsV2) -> dict:
    out: dict = {}
    if "ofi" in value:
        import aws_sdk_frauddetector.types.ofi_training_metrics_value

        out["ofi"] = (
            aws_sdk_frauddetector.types.ofi_training_metrics_value.serialize_aws_json_1_1(
                value["ofi"]
            )
        )
    if "tfi" in value:
        import aws_sdk_frauddetector.types.tfi_training_metrics_value

        out["tfi"] = (
            aws_sdk_frauddetector.types.tfi_training_metrics_value.serialize_aws_json_1_1(
                value["tfi"]
            )
        )
    if "ati" in value:
        import aws_sdk_frauddetector.types.ati_training_metrics_value

        out["ati"] = (
            aws_sdk_frauddetector.types.ati_training_metrics_value.serialize_aws_json_1_1(
                value["ati"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingMetricsV2:
    out: TrainingMetricsV2 = {}  # type: ignore[typeddict-item]
    if "ofi" in data:
        import aws_sdk_frauddetector.types.ofi_training_metrics_value

        out["ofi"] = (
            aws_sdk_frauddetector.types.ofi_training_metrics_value.deserialize_aws_json_1_1(
                data["ofi"]
            )
        )
    if "tfi" in data:
        import aws_sdk_frauddetector.types.tfi_training_metrics_value

        out["tfi"] = (
            aws_sdk_frauddetector.types.tfi_training_metrics_value.deserialize_aws_json_1_1(
                data["tfi"]
            )
        )
    if "ati" in data:
        import aws_sdk_frauddetector.types.ati_training_metrics_value

        out["ati"] = (
            aws_sdk_frauddetector.types.ati_training_metrics_value.deserialize_aws_json_1_1(
                data["ati"]
            )
        )
    return out
