"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#ListTelemetryPipelinesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.next_token
    import capo_observabilityadmin.types.telemetry_pipeline_summaries


class ListTelemetryPipelinesOutput(TypedDict, closed=True):
    pipeline_summaries: NotRequired[
        "capo_observabilityadmin.types.telemetry_pipeline_summaries.TelemetryPipelineSummaries"
    ]
    """<p>A list of telemetry pipeline summaries containing key information about each pipeline.</p>"""
    next_token: NotRequired["capo_observabilityadmin.types.next_token.NextToken"]
    """<p>A token to resume pagination of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTelemetryPipelinesOutput) -> dict:
    out: dict = {}
    if "pipeline_summaries" in value:
        import capo_observabilityadmin.types.telemetry_pipeline_summaries

        out["PipelineSummaries"] = (
            capo_observabilityadmin.types.telemetry_pipeline_summaries.serialize_json(
                value["pipeline_summaries"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTelemetryPipelinesOutput:
    out: ListTelemetryPipelinesOutput = {}  # type: ignore[typeddict-item]
    if "PipelineSummaries" in data:
        import capo_observabilityadmin.types.telemetry_pipeline_summaries

        out["pipeline_summaries"] = (
            capo_observabilityadmin.types.telemetry_pipeline_summaries.deserialize_json(
                data["PipelineSummaries"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
