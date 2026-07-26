"""Generated from Smithy shape ``com.amazonaws.xray#GetServiceGraphRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_xray.errors import DeserializationError

if TYPE_CHECKING:
    import capo_xray.types.group_arn
    import capo_xray.types.group_name
    import capo_xray.types.string
    import capo_xray.types.timestamp


class GetServiceGraphRequest(TypedDict, closed=True):
    start_time: "capo_xray.types.timestamp.Timestamp"
    """<p>The start of the time frame for which to generate a graph.</p>"""
    end_time: "capo_xray.types.timestamp.Timestamp"
    """<p>The end of the timeframe for which to generate a graph.</p>"""
    group_name: NotRequired["capo_xray.types.group_name.GroupName"]
    """<p>The name of a group based on which you want to generate a graph.</p>"""
    group_arn: NotRequired["capo_xray.types.group_arn.GroupARN"]
    """<p>The Amazon Resource Name (ARN) of a group based on which you want to generate a graph.</p>"""
    next_token: NotRequired["capo_xray.types.string.String"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceGraphRequest) -> dict:
    out: dict = {}
    import capo_xray.types.timestamp

    out["StartTime"] = capo_xray.types.timestamp.serialize_json(value["start_time"])
    import capo_xray.types.timestamp

    out["EndTime"] = capo_xray.types.timestamp.serialize_json(value["end_time"])
    if "group_name" in value:
        out["GroupName"] = value["group_name"]
    if "group_arn" in value:
        out["GroupARN"] = value["group_arn"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> GetServiceGraphRequest:
    out: GetServiceGraphRequest = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        import capo_xray.types.timestamp

        out["start_time"] = capo_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        raise DeserializationError("GetServiceGraphRequest.start_time required")
    if "EndTime" in data:
        import capo_xray.types.timestamp

        out["end_time"] = capo_xray.types.timestamp.deserialize_json(data["EndTime"])
    else:
        raise DeserializationError("GetServiceGraphRequest.end_time required")
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "GroupARN" in data:
        out["group_arn"] = data["GroupARN"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
