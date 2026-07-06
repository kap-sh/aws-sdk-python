"""Generated from Smithy shape ``com.amazonaws.connect#SearchContactsTimeRange``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.search_contacts_time_range_type
    import aws_sdk_connect.types.timestamp


class SearchContactsTimeRange(TypedDict, closed=True):
    type: "aws_sdk_connect.types.search_contacts_time_range_type.SearchContactsTimeRangeType"
    """<p>The type of timestamp to search.</p>"""
    start_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The start time of the time range.</p>"""
    end_time: "aws_sdk_connect.types.timestamp.Timestamp"
    """<p>The end time of the time range.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchContactsTimeRange) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.search_contacts_time_range_type

    out["Type"] = aws_sdk_connect.types.search_contacts_time_range_type.serialize_json(
        value["type"]
    )
    import aws_sdk_connect.types.timestamp

    out["StartTime"] = aws_sdk_connect.types.timestamp.serialize_json(
        value["start_time"]
    )
    import aws_sdk_connect.types.timestamp

    out["EndTime"] = aws_sdk_connect.types.timestamp.serialize_json(value["end_time"])
    return out


def deserialize_json(data: dict) -> SearchContactsTimeRange:
    out: SearchContactsTimeRange = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import aws_sdk_connect.types.search_contacts_time_range_type

        out["type"] = (
            aws_sdk_connect.types.search_contacts_time_range_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("SearchContactsTimeRange.type required")
    if "StartTime" in data:
        import aws_sdk_connect.types.timestamp

        out["start_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        raise DeserializationError("SearchContactsTimeRange.start_time required")
    if "EndTime" in data:
        import aws_sdk_connect.types.timestamp

        out["end_time"] = aws_sdk_connect.types.timestamp.deserialize_json(
            data["EndTime"]
        )
    else:
        raise DeserializationError("SearchContactsTimeRange.end_time required")
    return out
