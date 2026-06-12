"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationSnapshotConfigurationDescription``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.boolean_object


class ApplicationSnapshotConfigurationDescription(TypedDict):
    snapshots_enabled: "aws_sdk_kinesis_analytics_v2.types.boolean_object.BooleanObject"
    """<p>Describes whether snapshots are enabled for a Managed Service for Apache Flink application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationSnapshotConfigurationDescription) -> dict:
    out: dict = {}
    out["SnapshotsEnabled"] = value["snapshots_enabled"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationSnapshotConfigurationDescription:
    out: ApplicationSnapshotConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "SnapshotsEnabled" in data:
        out["snapshots_enabled"] = data["SnapshotsEnabled"]
    else:
        raise DeserializationError(
            "ApplicationSnapshotConfigurationDescription.snapshots_enabled required"
        )
    return out
