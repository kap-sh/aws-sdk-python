"""Generated from Smithy shape ``com.amazonaws.iotsitewise#Measurement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.measurement_processing_config


class Measurement(TypedDict, closed=True):
    processing_config: NotRequired[
        "aws_sdk_iotsitewise.types.measurement_processing_config.MeasurementProcessingConfig"
    ]
    """<p>The processing configuration for the given measurement property. You can configure measurements to be kept at the edge or forwarded to the Amazon Web Services Cloud. By default, measurements are forwarded to the cloud.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Measurement) -> dict:
    out: dict = {}
    if "processing_config" in value:
        import aws_sdk_iotsitewise.types.measurement_processing_config

        out["processingConfig"] = (
            aws_sdk_iotsitewise.types.measurement_processing_config.serialize_json(
                value["processing_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> Measurement:
    out: Measurement = {}  # type: ignore[typeddict-item]
    if "processingConfig" in data:
        import aws_sdk_iotsitewise.types.measurement_processing_config

        out["processing_config"] = (
            aws_sdk_iotsitewise.types.measurement_processing_config.deserialize_json(
                data["processingConfig"]
            )
        )
    return out
