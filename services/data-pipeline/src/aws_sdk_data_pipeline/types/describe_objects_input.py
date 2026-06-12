"""Generated from Smithy shape ``com.amazonaws.datapipeline#DescribeObjectsInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.boolean
    import aws_sdk_data_pipeline.types.id
    import aws_sdk_data_pipeline.types.id_list
    import aws_sdk_data_pipeline.types.string


class DescribeObjectsInput(TypedDict):
    pipeline_id: "aws_sdk_data_pipeline.types.id.id"
    """<p>The ID of the pipeline that contains the object definitions.</p>"""
    object_ids: "aws_sdk_data_pipeline.types.id_list.idList"
    """<p>The IDs of the pipeline objects that contain the definitions to be described. You can pass as many as 25 identifiers in a single call to <code>DescribeObjects</code>.</p>"""
    evaluate_expressions: "aws_sdk_data_pipeline.types.boolean.boolean"
    """<p>Indicates whether any expressions in the object should be evaluated when the object descriptions are returned.</p>"""
    marker: NotRequired["aws_sdk_data_pipeline.types.string.string"]
    """<p>The starting point for the results to be returned. For the first call, this value should be empty. As long as there are more results, continue to call <code>DescribeObjects</code> with the marker value from the previous call to retrieve the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeObjectsInput) -> dict:
    out: dict = {}
    out["pipelineId"] = value["pipeline_id"]
    import aws_sdk_data_pipeline.types.id_list

    out["objectIds"] = aws_sdk_data_pipeline.types.id_list.serialize_aws_json_1_1(
        value["object_ids"]
    )
    out["evaluateExpressions"] = value.get("evaluate_expressions", False)
    if "marker" in value:
        out["marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeObjectsInput:
    out: DescribeObjectsInput = {}  # type: ignore[typeddict-item]
    if "pipelineId" in data:
        out["pipeline_id"] = data["pipelineId"]
    else:
        raise DeserializationError("DescribeObjectsInput.pipeline_id required")
    if "objectIds" in data:
        import aws_sdk_data_pipeline.types.id_list

        out["object_ids"] = (
            aws_sdk_data_pipeline.types.id_list.deserialize_aws_json_1_1(
                data["objectIds"]
            )
        )
    else:
        raise DeserializationError("DescribeObjectsInput.object_ids required")
    if "evaluateExpressions" in data:
        out["evaluate_expressions"] = data["evaluateExpressions"]
    else:
        out["evaluate_expressions"] = False
    if "marker" in data:
        out["marker"] = data["marker"]
    return out
