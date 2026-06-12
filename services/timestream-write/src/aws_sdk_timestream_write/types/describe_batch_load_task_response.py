"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DescribeBatchLoadTaskResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_timestream_write.types.batch_load_task_description


class DescribeBatchLoadTaskResponse(TypedDict):
    batch_load_task_description: "aws_sdk_timestream_write.types.batch_load_task_description.BatchLoadTaskDescription"
    """<p>Description of the batch load task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeBatchLoadTaskResponse) -> dict:
    out: dict = {}
    import aws_sdk_timestream_write.types.batch_load_task_description

    out["BatchLoadTaskDescription"] = (
        aws_sdk_timestream_write.types.batch_load_task_description.serialize_aws_json_1_0(
            value["batch_load_task_description"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeBatchLoadTaskResponse:
    out: DescribeBatchLoadTaskResponse = {}  # type: ignore[typeddict-item]
    if "BatchLoadTaskDescription" in data:
        import aws_sdk_timestream_write.types.batch_load_task_description

        out["batch_load_task_description"] = (
            aws_sdk_timestream_write.types.batch_load_task_description.deserialize_aws_json_1_0(
                data["BatchLoadTaskDescription"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeBatchLoadTaskResponse.batch_load_task_description required"
        )
    return out
