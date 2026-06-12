"""Generated from Smithy shape ``com.amazonaws.opensearch#SnapshotOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_opensearch.types.integer_class


class SnapshotOptions(TypedDict):
    automated_snapshot_start_hour: NotRequired[
        "aws_sdk_opensearch.types.integer_class.IntegerClass"
    ]
    """<p>The time, in UTC format, when OpenSearch Service takes a daily automated snapshot of the specified domain. Default is <code>0</code> hours.</p>"""


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
