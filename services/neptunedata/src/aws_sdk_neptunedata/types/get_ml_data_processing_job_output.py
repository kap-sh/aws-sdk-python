"""Generated from Smithy shape ``com.amazonaws.neptunedata#GetMLDataProcessingJobOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_neptunedata.types.ml_resource_definition


class GetMLDataProcessingJobOutput(TypedDict):
    status: NotRequired["str"]
    """<p>Status of the data processing job.</p>"""
    id: NotRequired["str"]
    """<p>The unique identifier of this data-processing job.</p>"""
    processing_job: NotRequired[
        "aws_sdk_neptunedata.types.ml_resource_definition.MlResourceDefinition"
    ]
    """<p>Definition of the data processing job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetMLDataProcessingJobOutput) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "id" in value:
        out["id"] = value["id"]
    if "processing_job" in value:
        import aws_sdk_neptunedata.types.ml_resource_definition

        out["processingJob"] = (
            aws_sdk_neptunedata.types.ml_resource_definition.serialize_json(
                value["processing_job"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetMLDataProcessingJobOutput:
    out: GetMLDataProcessingJobOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "id" in data:
        out["id"] = data["id"]
    if "processingJob" in data:
        import aws_sdk_neptunedata.types.ml_resource_definition

        out["processing_job"] = (
            aws_sdk_neptunedata.types.ml_resource_definition.deserialize_json(
                data["processingJob"]
            )
        )
    return out
