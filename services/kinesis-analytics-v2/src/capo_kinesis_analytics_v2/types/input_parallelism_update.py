"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#InputParallelismUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.input_parallelism_count


class InputParallelismUpdate(TypedDict, closed=True):
    count_update: (
        "capo_kinesis_analytics_v2.types.input_parallelism_count.InputParallelismCount"
    )
    """<p>The number of in-application streams to create for the specified streaming source.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputParallelismUpdate) -> dict:
    out: dict = {}
    out["CountUpdate"] = value["count_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputParallelismUpdate:
    out: InputParallelismUpdate = {}  # type: ignore[typeddict-item]
    if "CountUpdate" in data:
        out["count_update"] = data["CountUpdate"]
    else:
        raise DeserializationError("InputParallelismUpdate.count_update required")
    return out
