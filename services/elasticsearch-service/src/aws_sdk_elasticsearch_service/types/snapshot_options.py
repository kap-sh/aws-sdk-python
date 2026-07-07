"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#SnapshotOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_elasticsearch_service.types.integer_class


class SnapshotOptions(TypedDict, closed=True):
    automated_snapshot_start_hour: NotRequired[
        "aws_sdk_elasticsearch_service.types.integer_class.IntegerClass"
    ]
    """<p>Specifies the time, in UTC format, when the service takes a daily automated snapshot of the specified Elasticsearch domain. Default value is <code>0</code> hours.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapshotOptions) -> dict:
    out: dict = {}
    if "automated_snapshot_start_hour" in value:
        out["AutomatedSnapshotStartHour"] = value["automated_snapshot_start_hour"]
    return out


def deserialize_json(data: dict) -> SnapshotOptions:
    out: SnapshotOptions = {}  # type: ignore[typeddict-item]
    if "AutomatedSnapshotStartHour" in data:
        out["automated_snapshot_start_hour"] = data["AutomatedSnapshotStartHour"]
    return out
