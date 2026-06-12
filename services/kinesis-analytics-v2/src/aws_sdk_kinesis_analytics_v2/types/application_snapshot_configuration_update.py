"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationSnapshotConfigurationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.boolean_object


class ApplicationSnapshotConfigurationUpdate(TypedDict):
    snapshots_enabled_update: (
        "aws_sdk_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    )
    """<p>Describes updates to whether snapshots are enabled for an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSnapshotConfigurationUpdate) -> dict:
    out: dict = {}
    out["SnapshotsEnabledUpdate"] = value["snapshots_enabled_update"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSnapshotConfigurationUpdate:
    out: ApplicationSnapshotConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "SnapshotsEnabledUpdate" in data:
        out["snapshots_enabled_update"] = data["SnapshotsEnabledUpdate"]
    else:
        raise DeserializationError(
            "ApplicationSnapshotConfigurationUpdate.snapshots_enabled_update required"
        )
    return out
