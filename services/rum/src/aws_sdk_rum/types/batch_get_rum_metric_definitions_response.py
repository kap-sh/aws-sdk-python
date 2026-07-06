"""Generated from Smithy shape ``com.amazonaws.rum#BatchGetRumMetricDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_rum.types.metric_definitions


class BatchGetRumMetricDefinitionsResponse(TypedDict, closed=True):
    metric_definitions: NotRequired[
        "aws_sdk_rum.types.metric_definitions.MetricDefinitions"
    ]
    """<p>An array of structures that display information about the metrics that are sent by the specified app monitor to the specified destination.</p>"""
    next_token: NotRequired["str"]
    """<p>A token that you can use in a subsequent operation to retrieve the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetRumMetricDefinitionsResponse) -> dict:
    out: dict = {}
    if "metric_definitions" in value:
        import aws_sdk_rum.types.metric_definitions

        out["MetricDefinitions"] = aws_sdk_rum.types.metric_definitions.serialize_json(
            value["metric_definitions"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> BatchGetRumMetricDefinitionsResponse:
    out: BatchGetRumMetricDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if "MetricDefinitions" in data:
        import aws_sdk_rum.types.metric_definitions

        out["metric_definitions"] = (
            aws_sdk_rum.types.metric_definitions.deserialize_json(
                data["MetricDefinitions"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
