"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationRestoreConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_restore_type
    import aws_sdk_kinesis_analytics_v2.types.snapshot_name


class ApplicationRestoreConfiguration(TypedDict):
    application_restore_type: "aws_sdk_kinesis_analytics_v2.types.application_restore_type.ApplicationRestoreType"
    """<p>Specifies how the application should be restored.</p>"""
    snapshot_name: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.snapshot_name.SnapshotName"
    ]
    """<p>The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if <code>RESTORE_FROM_CUSTOM_SNAPSHOT</code> is specified for the <code>ApplicationRestoreType</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationRestoreConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_kinesis_analytics_v2.types.application_restore_type

    out["ApplicationRestoreType"] = (
        aws_sdk_kinesis_analytics_v2.types.application_restore_type.serialize_aws_json_1_1(
            value["application_restore_type"]
        )
    )
    if "snapshot_name" in value:
        out["SnapshotName"] = value["snapshot_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationRestoreConfiguration:
    out: ApplicationRestoreConfiguration = {}  # type: ignore[typeddict-item]
    if "ApplicationRestoreType" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_restore_type

        out["application_restore_type"] = (
            aws_sdk_kinesis_analytics_v2.types.application_restore_type.deserialize_aws_json_1_1(
                data["ApplicationRestoreType"]
            )
        )
    else:
        raise DeserializationError(
            "ApplicationRestoreConfiguration.application_restore_type required"
        )
    if "SnapshotName" in data:
        out["snapshot_name"] = data["SnapshotName"]
    return out
