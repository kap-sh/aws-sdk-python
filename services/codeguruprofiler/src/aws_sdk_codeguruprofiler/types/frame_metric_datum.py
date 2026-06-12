"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#FrameMetricDatum``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.frame_metric
    import aws_sdk_codeguruprofiler.types.frame_metric_values


class FrameMetricDatum(TypedDict):
    frame_metric: "aws_sdk_codeguruprofiler.types.frame_metric.FrameMetric"
    values: "aws_sdk_codeguruprofiler.types.frame_metric_values.FrameMetricValues"
    """<p> A list of values that are associated with a frame metric. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FrameMetricDatum) -> dict:
    out: dict = {}
    import aws_sdk_codeguruprofiler.types.frame_metric

    out["frameMetric"] = aws_sdk_codeguruprofiler.types.frame_metric.serialize_json(
        value["frame_metric"]
    )
    import aws_sdk_codeguruprofiler.types.frame_metric_values

    out["values"] = aws_sdk_codeguruprofiler.types.frame_metric_values.serialize_json(
        value["values"]
    )
    return out


def deserialize_json(data: dict) -> FrameMetricDatum:
    out: FrameMetricDatum = {}  # type: ignore[typeddict-item]
    if "frameMetric" in data:
        import aws_sdk_codeguruprofiler.types.frame_metric

        out["frame_metric"] = (
            aws_sdk_codeguruprofiler.types.frame_metric.deserialize_json(
                data["frameMetric"]
            )
        )
    else:
        raise DeserializationError("FrameMetricDatum.frame_metric required")
    if "values" in data:
        import aws_sdk_codeguruprofiler.types.frame_metric_values

        out["values"] = (
            aws_sdk_codeguruprofiler.types.frame_metric_values.deserialize_json(
                data["values"]
            )
        )
    else:
        raise DeserializationError("FrameMetricDatum.values required")
    return out
