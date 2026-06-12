"""Generated from Smithy shape ``com.amazonaws.glue#OrphanFileDeletionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.iceberg_orphan_file_deletion_configuration


class OrphanFileDeletionConfiguration(TypedDict):
    iceberg_configuration: NotRequired[
        "aws_sdk_glue.types.iceberg_orphan_file_deletion_configuration.IcebergOrphanFileDeletionConfiguration"
    ]
    """<p>The configuration for an Iceberg orphan file deletion optimizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OrphanFileDeletionConfiguration) -> dict:
    out: dict = {}
    if "iceberg_configuration" in value:
        import aws_sdk_glue.types.iceberg_orphan_file_deletion_configuration

        out["icebergConfiguration"] = (
            aws_sdk_glue.types.iceberg_orphan_file_deletion_configuration.serialize_aws_json_1_1(
                value["iceberg_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OrphanFileDeletionConfiguration:
    out: OrphanFileDeletionConfiguration = {}  # type: ignore[typeddict-item]
    if "icebergConfiguration" in data:
        import aws_sdk_glue.types.iceberg_orphan_file_deletion_configuration

        out["iceberg_configuration"] = (
            aws_sdk_glue.types.iceberg_orphan_file_deletion_configuration.deserialize_aws_json_1_1(
                data["icebergConfiguration"]
            )
        )
    return out
