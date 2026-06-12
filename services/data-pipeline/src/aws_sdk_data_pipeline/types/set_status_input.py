"""Generated from Smithy shape ``com.amazonaws.datapipeline#SetStatusInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.id
    import aws_sdk_data_pipeline.types.id_list
    import aws_sdk_data_pipeline.types.string


class SetStatusInput(TypedDict):
    pipeline_id: "aws_sdk_data_pipeline.types.id.id"
    """<p>The ID of the pipeline that contains the objects.</p>"""
    object_ids: "aws_sdk_data_pipeline.types.id_list.idList"
    """<p>The IDs of the objects. The corresponding objects can be either physical or components, but not a mix of both types.</p>"""
    status: "aws_sdk_data_pipeline.types.string.string"
    """<p>The status to be set on all the objects specified in <code>objectIds</code>. For components, use <code>PAUSE</code> or <code>RESUME</code>. For instances, use <code>TRY_CANCEL</code>, <code>RERUN</code>, or <code>MARK_FINISHED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetStatusInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    import aws_sdk_data_pipeline.types.id_list

    out["objectIds"] = aws_sdk_data_pipeline.types.id_list.serialize_aws_json_1_1(
        value["object_ids"]
    )
    out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SetStatusInput:
    out: SetStatusInput = {}  # type: ignore[typeddict-item]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    else:
        raise DeserializationError("SetStatusInput.pipeline_id required")
    if "objectIds" in data:
        import aws_sdk_data_pipeline.types.id_list

        out["object_ids"] = (
            aws_sdk_data_pipeline.types.id_list.deserialize_aws_json_1_1(
                data["objectIds"]
            )
        )
    else:
        raise DeserializationError("SetStatusInput.object_ids required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("SetStatusInput.status required")
    return out
