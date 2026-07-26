"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#InputParallelism``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.input_parallelism_count


class InputParallelism(TypedDict, closed=True):
    count: NotRequired[
        "capo_kinesis_analytics_v2.types.input_parallelism_count.InputParallelismCount"
    ]
    """<p>The number of in-application streams to create.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputParallelism) -> dict:
    out: dict = {}
    if "count" in value:
        out["Count"] = value["count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> InputParallelism:
    out: InputParallelism = {}  # type: ignore[typeddict-item]
    if "Count" in data:
        out["count"] = data["Count"]
    return out
