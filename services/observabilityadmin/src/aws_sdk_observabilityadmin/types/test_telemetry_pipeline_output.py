"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TestTelemetryPipelineOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.pipeline_outputs


class TestTelemetryPipelineOutput(TypedDict):
    results: NotRequired[
        "aws_sdk_observabilityadmin.types.pipeline_outputs.PipelineOutputs"
    ]
    """<p>The results of processing the test records through the pipeline configuration, including any outputs or errors.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TestTelemetryPipelineOutput) -> dict:
    out: dict = {}
    if "results" in value:
        import aws_sdk_observabilityadmin.types.pipeline_outputs

        out["Results"] = (
            aws_sdk_observabilityadmin.types.pipeline_outputs.serialize_json(
                value["results"]
            )
        )
    return out


def deserialize_json(data: dict) -> TestTelemetryPipelineOutput:
    out: TestTelemetryPipelineOutput = {}  # type: ignore[typeddict-item]
    if "Results" in data:
        import aws_sdk_observabilityadmin.types.pipeline_outputs

        out["results"] = (
            aws_sdk_observabilityadmin.types.pipeline_outputs.deserialize_json(
                data["Results"]
            )
        )
    return out
