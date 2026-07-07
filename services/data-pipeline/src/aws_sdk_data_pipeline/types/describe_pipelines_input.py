"""Generated from Smithy shape ``com.amazonaws.datapipeline#DescribePipelinesInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.id_list


class DescribePipelinesInput(TypedDict, closed=True):
    pipeline_ids: "aws_sdk_data_pipeline.types.id_list.idList"
    """<p>The IDs of the pipelines to describe. You can pass as many as 25 identifiers in a single call. To obtain pipeline IDs, call <a>ListPipelines</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePipelinesInput) -> dict:
    out: dict = {}
    import aws_sdk_data_pipeline.types.id_list

    out["pipelineIds"] = aws_sdk_data_pipeline.types.id_list.serialize_aws_json_1_1(
        value["pipeline_ids"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePipelinesInput:
    out: DescribePipelinesInput = {}  # type: ignore[typeddict-item]
    if "pipelineIds" in data:
        import aws_sdk_data_pipeline.types.id_list

        out["pipeline_ids"] = (
            aws_sdk_data_pipeline.types.id_list.deserialize_aws_json_1_1(
                data["pipelineIds"]
            )
        )
    else:
        raise DeserializationError("DescribePipelinesInput.pipeline_ids required")
    return out
