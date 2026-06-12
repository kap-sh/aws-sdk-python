"""Generated from Smithy shape ``com.amazonaws.memorydb#Event``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_memorydb.types.source_type
    import aws_sdk_memorydb.types.string
    import aws_sdk_memorydb.types.t_stamp


class Event(TypedDict):
    source_name: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The name for the source of the event. For example, if the event occurred at the cluster level, the identifier would be the name of the cluster.</p>"""
    source_type: NotRequired["aws_sdk_memorydb.types.source_type.SourceType"]
    """<p>Specifies the origin of this event - a cluster, a parameter group, a security group, etc.</p>"""
    message: NotRequired["aws_sdk_memorydb.types.string.String"]
    """<p>The text of the event.</p>"""
    date: NotRequired["aws_sdk_memorydb.types.t_stamp.TStamp"]
    """<p>The date and time when the event occurred.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Event) -> dict:
    out: dict = {}
    if "source_name" in value:
        out["SourceName"] = value["source_name"]
    if "source_type" in value:
        import aws_sdk_memorydb.types.source_type

        out["SourceType"] = aws_sdk_memorydb.types.source_type.serialize_aws_json_1_1(
            value["source_type"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "date" in value:
        import aws_sdk_memorydb.types.t_stamp

        out["Date"] = aws_sdk_memorydb.types.t_stamp.serialize_aws_json_1_1(
            value["date"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if "SourceName" in data:
        out["source_name"] = data["SourceName"]
    if "SourceType" in data:
        import aws_sdk_memorydb.types.source_type

        out["source_type"] = (
            aws_sdk_memorydb.types.source_type.deserialize_aws_json_1_1(
                data["SourceType"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "Date" in data:
        import aws_sdk_memorydb.types.t_stamp

        out["date"] = aws_sdk_memorydb.types.t_stamp.deserialize_aws_json_1_1(
            data["Date"]
        )
    return out
