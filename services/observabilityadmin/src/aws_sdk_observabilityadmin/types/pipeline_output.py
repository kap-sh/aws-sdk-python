"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#PipelineOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_observabilityadmin.types.pipeline_output_error
    import aws_sdk_observabilityadmin.types.record


class PipelineOutput(TypedDict):
    record: NotRequired["aws_sdk_observabilityadmin.types.record.Record"]
    """<p>The processed record output from the pipeline test operation.</p>"""
    error: NotRequired[
        "aws_sdk_observabilityadmin.types.pipeline_output_error.PipelineOutputError"
    ]
    """<p>Any error that occurred during the pipeline test operation for this record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineOutput) -> dict:
    out: dict = {}
    if "record" in value:
        import aws_sdk_observabilityadmin.types.record

        out["Record"] = aws_sdk_observabilityadmin.types.record.serialize_json(
            value["record"]
        )
    if "error" in value:
        import aws_sdk_observabilityadmin.types.pipeline_output_error

        out["Error"] = (
            aws_sdk_observabilityadmin.types.pipeline_output_error.serialize_json(
                value["error"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipelineOutput:
    out: PipelineOutput = {}  # type: ignore[typeddict-item]
    if "Record" in data:
        import aws_sdk_observabilityadmin.types.record

        out["record"] = aws_sdk_observabilityadmin.types.record.deserialize_json(
            data["Record"]
        )
    if "Error" in data:
        import aws_sdk_observabilityadmin.types.pipeline_output_error

        out["error"] = (
            aws_sdk_observabilityadmin.types.pipeline_output_error.deserialize_json(
                data["Error"]
            )
        )
    return out
