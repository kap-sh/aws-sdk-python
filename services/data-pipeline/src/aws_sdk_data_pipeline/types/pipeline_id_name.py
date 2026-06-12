"""Generated from Smithy shape ``com.amazonaws.datapipeline#PipelineIdName``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.id


class PipelineIdName(TypedDict):
    id: NotRequired["aws_sdk_data_pipeline.types.id.id"]
    """<p>The ID of the pipeline that was assigned by AWS Data Pipeline. This is a string of the form <code>df-297EG78HU43EEXAMPLE</code>.</p>"""
    name: NotRequired["aws_sdk_data_pipeline.types.id.id"]
    """<p>The name of the pipeline.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PipelineIdName) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PipelineIdName:
    out: PipelineIdName = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    return out
