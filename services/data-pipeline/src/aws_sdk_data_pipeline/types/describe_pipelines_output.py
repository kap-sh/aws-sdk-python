"""Generated from Smithy shape ``com.amazonaws.datapipeline#DescribePipelinesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_data_pipeline.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_data_pipeline.types.pipeline_description_list


class DescribePipelinesOutput(TypedDict, closed=True):
    pipeline_description_list: (
        "aws_sdk_data_pipeline.types.pipeline_description_list.PipelineDescriptionList"
    )
    """<p>An array of descriptions for the specified pipelines.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribePipelinesOutput) -> dict:
    out: dict = {}
    import aws_sdk_data_pipeline.types.pipeline_description_list

    out["pipelineDescriptionList"] = (
        aws_sdk_data_pipeline.types.pipeline_description_list.serialize_aws_json_1_1(
            value["pipeline_description_list"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribePipelinesOutput:
    out: DescribePipelinesOutput = {}  # type: ignore[typeddict-item]
    if "pipelineDescriptionList" in data:
        import aws_sdk_data_pipeline.types.pipeline_description_list

        out["pipeline_description_list"] = (
            aws_sdk_data_pipeline.types.pipeline_description_list.deserialize_aws_json_1_1(
                data["pipelineDescriptionList"]
            )
        )
    else:
        raise DeserializationError(
            "DescribePipelinesOutput.pipeline_description_list required"
        )
    return out
