"""Generated from Smithy shape ``com.amazonaws.xray#GetServiceGraphRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_xray.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_xray.types.group_arn
    import aws_sdk_xray.types.group_name
    import aws_sdk_xray.types.string
    import aws_sdk_xray.types.timestamp


class GetServiceGraphRequest(TypedDict, closed=True):
    start_time: "aws_sdk_xray.types.timestamp.Timestamp"
    """<p>The start of the time frame for which to generate a graph.</p>"""
    end_time: "aws_sdk_xray.types.timestamp.Timestamp"
    """<p>The end of the timeframe for which to generate a graph.</p>"""
    group_name: NotRequired["aws_sdk_xray.types.group_name.GroupName"]
    """<p>The name of a group based on which you want to generate a graph.</p>"""
    group_arn: NotRequired["aws_sdk_xray.types.group_arn.GroupARN"]
    """<p>The Amazon Resource Name (ARN) of a group based on which you want to generate a graph.</p>"""
    next_token: NotRequired["aws_sdk_xray.types.string.String"]
    """<p>Pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceGraphRequest) -> dict:
    out: dict = {}
    import aws_sdk_xray.types.timestamp

    out["StartTime"] = aws_sdk_xray.types.timestamp.serialize_json(value["start_time"])
    import aws_sdk_xray.types.timestamp

    out["EndTime"] = aws_sdk_xray.types.timestamp.serialize_json(value["end_time"])
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
        import aws_sdk_xray.types.timestamp

        out["start_time"] = aws_sdk_xray.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        raise DeserializationError("GetServiceGraphRequest.start_time required")
    if "EndTime" in data:
        import aws_sdk_xray.types.timestamp

        out["end_time"] = aws_sdk_xray.types.timestamp.deserialize_json(data["EndTime"])
    else:
        raise DeserializationError("GetServiceGraphRequest.end_time required")
    if "GroupName" in data:
        out["group_name"] = data["GroupName"]
    if "GroupARN" in data:
        out["group_arn"] = data["GroupARN"]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
