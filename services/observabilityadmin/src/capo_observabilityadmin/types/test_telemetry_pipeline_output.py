"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TestTelemetryPipelineOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.pipeline_outputs


class TestTelemetryPipelineOutput(TypedDict, closed=True):
    results: NotRequired[
        "capo_observabilityadmin.types.pipeline_outputs.PipelineOutputs"
    ]
    """<p>The results of processing the test records through the pipeline configuration, including any outputs or errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestTelemetryPipelineOutput) -> dict:
    out: dict = {}
    if "results" in value:
        import capo_observabilityadmin.types.pipeline_outputs

        out["Results"] = capo_observabilityadmin.types.pipeline_outputs.serialize_json(
            value["results"]
        )
    return out


def deserialize_json(data: dict) -> TestTelemetryPipelineOutput:
    out: TestTelemetryPipelineOutput = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import capo_observabilityadmin.types.pipeline_outputs

        out["results"] = (
            capo_observabilityadmin.types.pipeline_outputs.deserialize_json(
                data["Results"]
            )
        )
    return out
