"""Generated from Smithy shape ``com.amazonaws.sfn#MapRunStartedEventDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sfn.types.long_arn


class MapRunStartedEventDetails(TypedDict, closed=True):
    map_run_arn: NotRequired["capo_sfn.types.long_arn.LongArn"]
    """<p>The Amazon Resource Name (ARN) of a Map Run that was started.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MapRunStartedEventDetails) -> dict:
    out: dict = {}
    if "map_run_arn" in value:
        out["mapRunArn"] = value["map_run_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MapRunStartedEventDetails:
    out: MapRunStartedEventDetails = {}  # type: ignore[typeddict-item]
    if data.get("mapRunArn") is not None:
        out["map_run_arn"] = data["mapRunArn"]
    return out
