"""Generated from Smithy shape ``com.amazonaws.devopsguru#DescribeAccountOverviewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_guru.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.timestamp


class DescribeAccountOverviewRequest(TypedDict, closed=True):
    from_time: "aws_sdk_devops_guru.types.timestamp.Timestamp"
    """<p> The start of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred after this day. </p>"""
    to_time: NotRequired["aws_sdk_devops_guru.types.timestamp.Timestamp"]
    """<p> The end of the time range passed in. The start time granularity is at the day level. The floor of the start time is used. Returned information occurred before this day. If this is not specified, then the current day is used. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAccountOverviewRequest) -> dict:
    out: dict = {}
    import aws_sdk_devops_guru.types.timestamp

    out["FromTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
        value["from_time"]
    )
    if "to_time" in value:
        import aws_sdk_devops_guru.types.timestamp

        out["ToTime"] = aws_sdk_devops_guru.types.timestamp.serialize_json(
            value["to_time"]
        )
    return out


def deserialize_json(data: dict) -> DescribeAccountOverviewRequest:
    out: DescribeAccountOverviewRequest = {}  # type: ignore[typeddict-item]
    if "FromTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["from_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["FromTime"]
        )
    else:
        raise DeserializationError("DescribeAccountOverviewRequest.from_time required")
    if "ToTime" in data:
        import aws_sdk_devops_guru.types.timestamp

        out["to_time"] = aws_sdk_devops_guru.types.timestamp.deserialize_json(
            data["ToTime"]
        )
    return out
