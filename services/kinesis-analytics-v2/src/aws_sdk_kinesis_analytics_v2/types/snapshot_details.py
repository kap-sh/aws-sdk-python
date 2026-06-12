"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#SnapshotDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_description
    import aws_sdk_kinesis_analytics_v2.types.application_version_id
    import aws_sdk_kinesis_analytics_v2.types.runtime_environment
    import aws_sdk_kinesis_analytics_v2.types.snapshot_name
    import aws_sdk_kinesis_analytics_v2.types.snapshot_status
    import aws_sdk_kinesis_analytics_v2.types.timestamp


class SnapshotDetails(TypedDict):
    snapshot_name: "aws_sdk_kinesis_analytics_v2.types.snapshot_name.SnapshotName"
    """<p>The identifier for the application snapshot.</p>"""
    snapshot_status: "aws_sdk_kinesis_analytics_v2.types.snapshot_status.SnapshotStatus"
    """<p>The status of the application snapshot.</p>"""
    application_version_id: (
        "aws_sdk_kinesis_analytics_v2.types.application_version_id.ApplicationVersionId"
    )
    """<p>The current application version ID when the snapshot was created.</p>"""
    snapshot_creation_timestamp: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.timestamp.Timestamp"
    ]
    """<p>The timestamp of the application snapshot.</p>"""
    runtime_environment: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.runtime_environment.RuntimeEnvironment"
    ]
    """<p>The Flink Runtime for the application snapshot.</p>"""
    application_encryption_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_description.ApplicationEncryptionConfigurationDescription"
    ]
    """<p>Specifies the encryption settings of data at rest for the application snapshot.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SnapshotDetails) -> dict:
    out: dict = {}
    out["SnapshotName"] = value["snapshot_name"]
    import aws_sdk_kinesis_analytics_v2.types.snapshot_status

    out["SnapshotStatus"] = (
        aws_sdk_kinesis_analytics_v2.types.snapshot_status.serialize_aws_json_1_1(
            value["snapshot_status"]
        )
    )
    out["ApplicationVersionId"] = value["application_version_id"]
    if "snapshot_creation_timestamp" in value:
        import aws_sdk_kinesis_analytics_v2.types.timestamp

        out["SnapshotCreationTimestamp"] = (
            aws_sdk_kinesis_analytics_v2.types.timestamp.serialize_aws_json_1_1(
                value["snapshot_creation_timestamp"]
            )
        )
    if "runtime_environment" in value:
        import aws_sdk_kinesis_analytics_v2.types.runtime_environment

        out["RuntimeEnvironment"] = (
            aws_sdk_kinesis_analytics_v2.types.runtime_environment.serialize_aws_json_1_1(
                value["runtime_environment"]
            )
        )
    if "application_encryption_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_description

        out["ApplicationEncryptionConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_description.serialize_aws_json_1_1(
                value["application_encryption_configuration_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SnapshotDetails:
    out: SnapshotDetails = {}  # type: ignore[typeddict-item]
    if "SnapshotName" in data:
        out["snapshot_name"] = data["SnapshotName"]
    else:
        raise DeserializationError("SnapshotDetails.snapshot_name required")
    if "SnapshotStatus" in data:
        import aws_sdk_kinesis_analytics_v2.types.snapshot_status

        out["snapshot_status"] = (
            aws_sdk_kinesis_analytics_v2.types.snapshot_status.deserialize_aws_json_1_1(
                data["SnapshotStatus"]
            )
        )
    else:
        raise DeserializationError("SnapshotDetails.snapshot_status required")
    if "ApplicationVersionId" in data:
        out["application_version_id"] = data["ApplicationVersionId"]
    else:
        raise DeserializationError("SnapshotDetails.application_version_id required")
    if "SnapshotCreationTimestamp" in data:
        import aws_sdk_kinesis_analytics_v2.types.timestamp

        out["snapshot_creation_timestamp"] = (
            aws_sdk_kinesis_analytics_v2.types.timestamp.deserialize_aws_json_1_1(
                data["SnapshotCreationTimestamp"]
            )
        )
    if "RuntimeEnvironment" in data:
        import aws_sdk_kinesis_analytics_v2.types.runtime_environment

        out["runtime_environment"] = (
            aws_sdk_kinesis_analytics_v2.types.runtime_environment.deserialize_aws_json_1_1(
                data["RuntimeEnvironment"]
            )
        )
    if "ApplicationEncryptionConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_description

        out["application_encryption_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_description.deserialize_aws_json_1_1(
                data["ApplicationEncryptionConfigurationDescription"]
            )
        )
    return out
