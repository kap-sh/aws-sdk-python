"""Generated from Smithy shape ``com.amazonaws.kinesisanalytics#InputParallelismUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics.types.input_parallelism_count


class InputParallelismUpdate(TypedDict, closed=True):
    count_update: NotRequired[
        "capo_kinesis_analytics.types.input_parallelism_count.InputParallelismCount"
    ]
    """<p>Number of in-application streams to create for the specified streaming source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputParallelismUpdate) -> dict:
    out: dict = {}
    if "count_update" in value:
        out["CountUpdate"] = value["count_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputParallelismUpdate:
    out: InputParallelismUpdate = {}  # type: ignore[typeddict-item]
    if "CountUpdate" in data:
        out["count_update"] = data["CountUpdate"]
    return out
