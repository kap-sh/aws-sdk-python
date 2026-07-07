"""Generated from Smithy shape ``com.amazonaws.glue#TableOptimizerConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.arn_string
    import aws_sdk_glue.types.compaction_configuration
    import aws_sdk_glue.types.nullable_boolean
    import aws_sdk_glue.types.orphan_file_deletion_configuration
    import aws_sdk_glue.types.retention_configuration
    import aws_sdk_glue.types.table_optimizer_vpc_configuration


class TableOptimizerConfiguration(TypedDict, closed=True):
    role_arn: NotRequired["aws_sdk_glue.types.arn_string.ArnString"]
    """<p>A role passed by the caller which gives the service permission to update the resources associated with the optimizer on the caller's behalf.</p>"""
    enabled: NotRequired["aws_sdk_glue.types.nullable_boolean.NullableBoolean"]
    """<p>Whether table optimization is enabled.</p>"""
    vpc_configuration: NotRequired[
        "aws_sdk_glue.types.table_optimizer_vpc_configuration.TableOptimizerVpcConfiguration"
    ]
    """<p>A <code>TableOptimizerVpcConfiguration</code> object representing the VPC configuration for a table optimizer.</p> <p>This configuration is necessary to perform optimization on tables that are in a customer VPC.</p>"""
    compaction_configuration: NotRequired[
        "aws_sdk_glue.types.compaction_configuration.CompactionConfiguration"
    ]
    """<p>The configuration for a compaction optimizer. This configuration defines how data files in your table will be compacted to improve query performance and reduce storage costs.</p>"""
    retention_configuration: NotRequired[
        "aws_sdk_glue.types.retention_configuration.RetentionConfiguration"
    ]
    """<p>The configuration for a snapshot retention optimizer.</p>"""
    orphan_file_deletion_configuration: NotRequired[
        "aws_sdk_glue.types.orphan_file_deletion_configuration.OrphanFileDeletionConfiguration"
    ]
    """<p>The configuration for an orphan file deletion optimizer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableOptimizerConfiguration) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["roleArn"] = value["role_arn"]
    if "enabled" in value:
        out["enabled"] = value["enabled"]
    if "vpc_configuration" in value:
        import aws_sdk_glue.types.table_optimizer_vpc_configuration

        out["vpcConfiguration"] = (
            aws_sdk_glue.types.table_optimizer_vpc_configuration.serialize_aws_json_1_1(
                value["vpc_configuration"]
            )
        )
    if "compaction_configuration" in value:
        import aws_sdk_glue.types.compaction_configuration

        out["compactionConfiguration"] = (
            aws_sdk_glue.types.compaction_configuration.serialize_aws_json_1_1(
                value["compaction_configuration"]
            )
        )
    if "retention_configuration" in value:
        import aws_sdk_glue.types.retention_configuration

        out["retentionConfiguration"] = (
            aws_sdk_glue.types.retention_configuration.serialize_aws_json_1_1(
                value["retention_configuration"]
            )
        )
    if "orphan_file_deletion_configuration" in value:
        import aws_sdk_glue.types.orphan_file_deletion_configuration

        out["orphanFileDeletionConfiguration"] = (
            aws_sdk_glue.types.orphan_file_deletion_configuration.serialize_aws_json_1_1(
                value["orphan_file_deletion_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TableOptimizerConfiguration:
    out: TableOptimizerConfiguration = {}  # type: ignore[typeddict-item]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    if "enabled" in data:
        out["enabled"] = data["enabled"]
    if "vpcConfiguration" in data:
        import aws_sdk_glue.types.table_optimizer_vpc_configuration

        out["vpc_configuration"] = (
            aws_sdk_glue.types.table_optimizer_vpc_configuration.deserialize_aws_json_1_1(
                data["vpcConfiguration"]
            )
        )
    if "compactionConfiguration" in data:
        import aws_sdk_glue.types.compaction_configuration

        out["compaction_configuration"] = (
            aws_sdk_glue.types.compaction_configuration.deserialize_aws_json_1_1(
                data["compactionConfiguration"]
            )
        )
    if "retentionConfiguration" in data:
        import aws_sdk_glue.types.retention_configuration

        out["retention_configuration"] = (
            aws_sdk_glue.types.retention_configuration.deserialize_aws_json_1_1(
                data["retentionConfiguration"]
            )
        )
    if "orphanFileDeletionConfiguration" in data:
        import aws_sdk_glue.types.orphan_file_deletion_configuration

        out["orphan_file_deletion_configuration"] = (
            aws_sdk_glue.types.orphan_file_deletion_configuration.deserialize_aws_json_1_1(
                data["orphanFileDeletionConfiguration"]
            )
        )
    return out
