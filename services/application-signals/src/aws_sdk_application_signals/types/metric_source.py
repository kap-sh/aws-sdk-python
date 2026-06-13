"""Generated from Smithy shape ``com.amazonaws.applicationsignals#MetricSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_application_signals.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_application_signals.types.attributes


class MetricSource(TypedDict):
    metric_source_key_attributes: (
        "aws_sdk_application_signals.types.attributes.Attributes"
    )
    """<p>Key attributes that identify the metric source.</p>"""
    metric_source_attributes: NotRequired[
        "aws_sdk_application_signals.types.attributes.Attributes"
    ]
    """<p>Additional attributes for the metric source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetricSource) -> dict:
    out: dict = {}
    import aws_sdk_application_signals.types.attributes

    out["MetricSourceKeyAttributes"] = (
        aws_sdk_application_signals.types.attributes.serialize_json(
            value["metric_source_key_attributes"]
        )
    )
    if "metric_source_attributes" in value:
        import aws_sdk_application_signals.types.attributes

        out["MetricSourceAttributes"] = (
            aws_sdk_application_signals.types.attributes.serialize_json(
                value["metric_source_attributes"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetricSource:
    out: MetricSource = {}  # type: ignore[typeddict-item]
    if "MetricSourceKeyAttributes" in data:
        import aws_sdk_application_signals.types.attributes

        out["metric_source_key_attributes"] = (
            aws_sdk_application_signals.types.attributes.deserialize_json(
                data["MetricSourceKeyAttributes"]
            )
        )
    else:
        raise DeserializationError("MetricSource.metric_source_key_attributes required")
    if "MetricSourceAttributes" in data:
        import aws_sdk_application_signals.types.attributes

        out["metric_source_attributes"] = (
            aws_sdk_application_signals.types.attributes.deserialize_json(
                data["MetricSourceAttributes"]
            )
        )
    return out
