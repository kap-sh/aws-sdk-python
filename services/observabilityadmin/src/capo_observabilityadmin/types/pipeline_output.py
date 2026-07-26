"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#PipelineOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.pipeline_output_error
    import capo_observabilityadmin.types.record


class PipelineOutput(TypedDict, closed=True):
    record: NotRequired["capo_observabilityadmin.types.record.Record"]
    """<p>The processed record output from the pipeline test operation.</p>"""
    error: NotRequired[
        "capo_observabilityadmin.types.pipeline_output_error.PipelineOutputError"
    ]
    """<p>Any error that occurred during the pipeline test operation for this record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineOutput) -> dict:
    out: dict = {}
    if "record" in value:
        import capo_observabilityadmin.types.record

        out["Record"] = capo_observabilityadmin.types.record.serialize_json(
            value["record"]
        )
    if "error" in value:
        import capo_observabilityadmin.types.pipeline_output_error

        out["Error"] = (
            capo_observabilityadmin.types.pipeline_output_error.serialize_json(
                value["error"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipelineOutput:
    out: PipelineOutput = {}  # type: ignore[typeddict-item]
    if "Record" in data:
        import capo_observabilityadmin.types.record

        out["record"] = capo_observabilityadmin.types.record.deserialize_json(
            data["Record"]
        )
    if "Error" in data:
        import capo_observabilityadmin.types.pipeline_output_error

        out["error"] = (
            capo_observabilityadmin.types.pipeline_output_error.deserialize_json(
                data["Error"]
            )
        )
    return out
