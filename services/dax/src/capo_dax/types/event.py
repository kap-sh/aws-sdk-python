"""Generated from Smithy shape ``com.amazonaws.dax#Event``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_dax.types.source_type
    import capo_dax.types.string
    import capo_dax.types.t_stamp


class Event(TypedDict, closed=True):
    source_name: NotRequired["capo_dax.types.string.String"]
    """<p>The source of the event. For example, if the event occurred at the node level, the source would be the node ID.</p>"""
    source_type: NotRequired["capo_dax.types.source_type.SourceType"]
    """<p>Specifies the origin of this event - a cluster, a parameter group, a node ID, etc.</p>"""
    message: NotRequired["capo_dax.types.string.String"]
    """<p>A user-defined message associated with the event.</p>"""
    date: NotRequired["capo_dax.types.t_stamp.TStamp"]
    """<p>The date and time when the event occurred.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Event) -> dict:
    out: dict = {}
    if "source_name" in value:
        out["SourceName"] = value["source_name"]
    if "source_type" in value:
        import capo_dax.types.source_type

        out["SourceType"] = capo_dax.types.source_type.serialize_aws_json_1_1(
            value["source_type"]
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "date" in value:
        import capo_dax.types.t_stamp

        out["Date"] = capo_dax.types.t_stamp.serialize_aws_json_1_1(value["date"])
    return out


def deserialize_aws_json_1_1(data: dict) -> Event:
    out: Event = {}  # type: ignore[typeddict-item]
    if "SourceName" in data:
        out["source_name"] = data["SourceName"]
    if "SourceType" in data:
        import capo_dax.types.source_type

        out["source_type"] = capo_dax.types.source_type.deserialize_aws_json_1_1(
            data["SourceType"]
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "Date" in data:
        import capo_dax.types.t_stamp

        out["date"] = capo_dax.types.t_stamp.deserialize_aws_json_1_1(data["Date"])
    return out
