"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListTelemetryPipelinesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.list_telemetry_pipelines_max_results
    import aws_sdk_observabilityadmin.types.next_token


class ListTelemetryPipelinesInput(TypedDict, closed=True):
    max_results: NotRequired[
        "aws_sdk_observabilityadmin.types.list_telemetry_pipelines_max_results.ListTelemetryPipelinesMaxResults"
    ]
    """<p>The maximum number of telemetry pipelines to return in a single call.</p>"""
    next_token: NotRequired["aws_sdk_observabilityadmin.types.next_token.NextToken"]
    """<p>The token for the next set of results. A previous call generates this token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTelemetryPipelinesInput) -> dict:
    out: dict = {}
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTelemetryPipelinesInput:
    out: ListTelemetryPipelinesInput = {}  # type: ignore[typeddict-item]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
