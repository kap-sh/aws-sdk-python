"""Generated from Smithy shape ``com.amazonaws.iotsitewise#MetricProcessingConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsitewise.types.compute_location


class MetricProcessingConfig(TypedDict, closed=True):
    compute_location: "aws_sdk_iotsitewise.types.compute_location.ComputeLocation"
    """<p>The compute location for the given metric property. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricProcessingConfig) -> dict:
    out: dict = {}
    import aws_sdk_iotsitewise.types.compute_location

    out["computeLocation"] = aws_sdk_iotsitewise.types.compute_location.serialize_json(
        value["compute_location"]
    )
    return out


def deserialize_json(data: dict) -> MetricProcessingConfig:
    out: MetricProcessingConfig = {}  # type: ignore[typeddict-item]
    if "computeLocation" in data:
        import aws_sdk_iotsitewise.types.compute_location

        out["compute_location"] = (
            aws_sdk_iotsitewise.types.compute_location.deserialize_json(
                data["computeLocation"]
            )
        )
    else:
        raise DeserializationError("MetricProcessingConfig.compute_location required")
    return out
