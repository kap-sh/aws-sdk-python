"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#UpdateSnapshotCopyConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_redshift_serverless.errors import DeserializationError

if TYPE_CHECKING:
    import capo_redshift_serverless.types.snapshot_copy_configuration


class UpdateSnapshotCopyConfigurationResponse(TypedDict, closed=True):
    snapshot_copy_configuration: "capo_redshift_serverless.types.snapshot_copy_configuration.SnapshotCopyConfiguration"
    """<p>The updated snapshot copy configuration object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSnapshotCopyConfigurationResponse) -> dict:
    out: dict = {}
    import capo_redshift_serverless.types.snapshot_copy_configuration

    out["snapshotCopyConfiguration"] = (
        capo_redshift_serverless.types.snapshot_copy_configuration.serialize_aws_json_1_1(
            value["snapshot_copy_configuration"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSnapshotCopyConfigurationResponse:
    out: UpdateSnapshotCopyConfigurationResponse = {}  # type: ignore[typeddict-item]
    if "snapshotCopyConfiguration" in data:
        import capo_redshift_serverless.types.snapshot_copy_configuration

        out["snapshot_copy_configuration"] = (
            capo_redshift_serverless.types.snapshot_copy_configuration.deserialize_aws_json_1_1(
                data["snapshotCopyConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateSnapshotCopyConfigurationResponse.snapshot_copy_configuration required"
        )
    return out
