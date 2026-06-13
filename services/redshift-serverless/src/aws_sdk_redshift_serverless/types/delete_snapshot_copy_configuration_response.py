"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#DeleteSnapshotCopyConfigurationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.snapshot_copy_configuration


class DeleteSnapshotCopyConfigurationResponse(TypedDict):
    snapshot_copy_configuration: "aws_sdk_redshift_serverless.types.snapshot_copy_configuration.SnapshotCopyConfiguration"
    """<p>The deleted snapshot copy configuration object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSnapshotCopyConfigurationResponse) -> dict:
    out: dict = {}
    import aws_sdk_redshift_serverless.types.snapshot_copy_configuration

    out["snapshotCopyConfiguration"] = (
        aws_sdk_redshift_serverless.types.snapshot_copy_configuration.serialize_aws_json_1_1(
            value["snapshot_copy_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSnapshotCopyConfigurationResponse:
    out: DeleteSnapshotCopyConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "snapshotCopyConfiguration" in data:
        import aws_sdk_redshift_serverless.types.snapshot_copy_configuration

        out["snapshot_copy_configuration"] = (
            aws_sdk_redshift_serverless.types.snapshot_copy_configuration.deserialize_aws_json_1_1(
                data["snapshotCopyConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "DeleteSnapshotCopyConfigurationResponse.snapshot_copy_configuration required"
        )
    return out
