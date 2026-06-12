"""Generated from Smithy shape ``com.amazonaws.sfn#MapRunRedrivenEventDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sfn.types.long_arn
    import aws_sdk_sfn.types.redrive_count


class MapRunRedrivenEventDetails(TypedDict):
    map_run_arn: NotRequired["aws_sdk_sfn.types.long_arn.LongArn"]
    """<p>The Amazon Resource Name (ARN) of a Map Run that was redriven.</p>"""
    redrive_count: NotRequired["aws_sdk_sfn.types.redrive_count.RedriveCount"]
    """<p>The number of times the Map Run has been redriven at this point in the execution's history including this event. The redrive count for a redriven Map Run is always greater than 0.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MapRunRedrivenEventDetails) -> dict:
    out: dict = {}
    if "map_run_arn" in value:
        out["mapRunArn"] = value["map_run_arn"]
    if "redrive_count" in value:
        out["redriveCount"] = value["redrive_count"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MapRunRedrivenEventDetails:
    out: MapRunRedrivenEventDetails = {}  # type: ignore[typeddict-item]
    if "mapRunArn" in data:
        out["map_run_arn"] = data["mapRunArn"]
    if "redriveCount" in data:
        out["redrive_count"] = data["redriveCount"]
    return out
