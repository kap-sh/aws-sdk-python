"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AutomatedSnapshotPauseRequestOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticsearch_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.boolean
    import aws_sdk_elasticsearch_service.types.update_timestamp


class AutomatedSnapshotPauseRequestOptions(TypedDict):
    enabled: "aws_sdk_elasticsearch_service.types.boolean.Boolean"
    """<p>Whether to enable or disable automated snapshot pause for the domain.</p>"""
    start_time: NotRequired[
        "aws_sdk_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The timestamp at which the automated snapshot pause should begin.</p>"""
    end_time: NotRequired[
        "aws_sdk_elasticsearch_service.types.update_timestamp.UpdateTimestamp"
    ]
    """<p>The timestamp at which the automated snapshot pause should end. The maximum allowed duration between <code>StartTime</code> and <code>EndTime</code> is 3 days.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedSnapshotPauseRequestOptions) -> dict:
    out: dict = {}
    out["Enabled"] = value["enabled"]
    if "start_time" in value:
        import aws_sdk_elasticsearch_service.types.update_timestamp

        out["StartTime"] = (
            aws_sdk_elasticsearch_service.types.update_timestamp.serialize_json(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_elasticsearch_service.types.update_timestamp

        out["EndTime"] = (
            aws_sdk_elasticsearch_service.types.update_timestamp.serialize_json(
                value["end_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedSnapshotPauseRequestOptions:
    out: AutomatedSnapshotPauseRequestOptions = {}  # type: ignore[typeddict-item]
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    else:
        raise DeserializationError(
            "AutomatedSnapshotPauseRequestOptions.enabled required"
        )
    if "StartTime" in data:
        import aws_sdk_elasticsearch_service.types.update_timestamp

        out["start_time"] = (
            aws_sdk_elasticsearch_service.types.update_timestamp.deserialize_json(
                data["StartTime"]
            )
        )
    if "EndTime" in data:
        import aws_sdk_elasticsearch_service.types.update_timestamp

        out["end_time"] = (
            aws_sdk_elasticsearch_service.types.update_timestamp.deserialize_json(
                data["EndTime"]
            )
        )
    return out
