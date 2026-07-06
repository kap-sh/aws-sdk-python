"""Generated from Smithy shape ``com.amazonaws.notifications#SummarizationDimensionOverview``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_notifications.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_notifications.types.sample_aggregation_dimension_values


class SummarizationDimensionOverview(TypedDict, closed=True):
    name: "str"
    """<p>Name of the summarization dimension.</p>"""
    count: "int"
    """<p>Total number of occurrences for this dimension.</p>"""
    sample_values: NotRequired[
        "aws_sdk_notifications.types.sample_aggregation_dimension_values.SampleAggregationDimensionValues"
    ]
    """<p>Indicates the sample values found within the dimension.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SummarizationDimensionOverview) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    out["count"] = value["count"]
    if "sample_values" in value:
        import aws_sdk_notifications.types.sample_aggregation_dimension_values

        out["sampleValues"] = (
            aws_sdk_notifications.types.sample_aggregation_dimension_values.serialize_json(
                value["sample_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> SummarizationDimensionOverview:
    out: SummarizationDimensionOverview = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("SummarizationDimensionOverview.name required")
    if "count" in data:
        out["count"] = data["count"]
    else:
        raise DeserializationError("SummarizationDimensionOverview.count required")
    if "sampleValues" in data:
        import aws_sdk_notifications.types.sample_aggregation_dimension_values

        out["sample_values"] = (
            aws_sdk_notifications.types.sample_aggregation_dimension_values.deserialize_json(
                data["sampleValues"]
            )
        )
    return out
