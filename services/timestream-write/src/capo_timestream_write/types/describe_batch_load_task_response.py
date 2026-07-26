"""Generated from Smithy shape ``com.amazonaws.timestreamwrite#DescribeBatchLoadTaskResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_timestream_write.errors import DeserializationError

if TYPE_CHECKING:
    import capo_timestream_write.types.batch_load_task_description


class DescribeBatchLoadTaskResponse(TypedDict, closed=True):
    batch_load_task_description: "capo_timestream_write.types.batch_load_task_description.BatchLoadTaskDescription"
    """<p>Description of the batch load task.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeBatchLoadTaskResponse) -> dict:
    out: dict = {}
    import capo_timestream_write.types.batch_load_task_description

    out["BatchLoadTaskDescription"] = (
        capo_timestream_write.types.batch_load_task_description.serialize_aws_json_1_0(
            value["batch_load_task_description"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeBatchLoadTaskResponse:
    out: DescribeBatchLoadTaskResponse = {}  # type: ignore[typeddict-item]
    if "BatchLoadTaskDescription" in data:
        import capo_timestream_write.types.batch_load_task_description

        out["batch_load_task_description"] = (
            capo_timestream_write.types.batch_load_task_description.deserialize_aws_json_1_0(
                data["BatchLoadTaskDescription"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeBatchLoadTaskResponse.batch_load_task_description required"
        )
    return out
