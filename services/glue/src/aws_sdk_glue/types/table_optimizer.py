"""Generated from Smithy shape ``com.amazonaws.glue#TableOptimizer``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.configuration_source
    import aws_sdk_glue.types.table_optimizer_configuration
    import aws_sdk_glue.types.table_optimizer_run
    import aws_sdk_glue.types.table_optimizer_type


class TableOptimizer(TypedDict):
    type: NotRequired["aws_sdk_glue.types.table_optimizer_type.TableOptimizerType"]
    """<p>The type of table optimizer. The valid values are:</p> <ul> <li> <p> <code>compaction</code>: for managing compaction with a table optimizer.</p> </li> <li> <p> <code>retention</code>: for managing the retention of snapshot with a table optimizer.</p> </li> <li> <p> <code>orphan_file_deletion</code>: for managing the deletion of orphan files with a table optimizer.</p> </li> </ul>"""
    configuration: NotRequired[
        "aws_sdk_glue.types.table_optimizer_configuration.TableOptimizerConfiguration"
    ]
    """<p>A <code>TableOptimizerConfiguration</code> object that was specified when creating or updating a table optimizer.</p>"""
    last_run: NotRequired["aws_sdk_glue.types.table_optimizer_run.TableOptimizerRun"]
    """<p>A <code>TableOptimizerRun</code> object representing the last run of the table optimizer.</p>"""
    configuration_source: NotRequired[
        "aws_sdk_glue.types.configuration_source.ConfigurationSource"
    ]
    """<p> Specifies the source of the optimizer configuration. This indicates how the table optimizer was configured and which entity or service initiated the configuration. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TableOptimizer) -> dict:
    out: dict = {}
    if "type" in value:
        import aws_sdk_glue.types.table_optimizer_type

        out["type"] = aws_sdk_glue.types.table_optimizer_type.serialize_aws_json_1_1(
            value["type"]
        )
    if "configuration" in value:
        import aws_sdk_glue.types.table_optimizer_configuration

        out["configuration"] = (
            aws_sdk_glue.types.table_optimizer_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "last_run" in value:
        import aws_sdk_glue.types.table_optimizer_run

        out["lastRun"] = aws_sdk_glue.types.table_optimizer_run.serialize_aws_json_1_1(
            value["last_run"]
        )
    if "configuration_source" in value:
        import aws_sdk_glue.types.configuration_source

        out["configurationSource"] = (
            aws_sdk_glue.types.configuration_source.serialize_aws_json_1_1(
                value["configuration_source"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TableOptimizer:
    out: TableOptimizer = {}  # type: ignore[typeddict-item]
    if "type" in data:
        import aws_sdk_glue.types.table_optimizer_type

        out["type"] = aws_sdk_glue.types.table_optimizer_type.deserialize_aws_json_1_1(
            data["type"]
        )
    if "configuration" in data:
        import aws_sdk_glue.types.table_optimizer_configuration

        out["configuration"] = (
            aws_sdk_glue.types.table_optimizer_configuration.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    if "lastRun" in data:
        import aws_sdk_glue.types.table_optimizer_run

        out["last_run"] = (
            aws_sdk_glue.types.table_optimizer_run.deserialize_aws_json_1_1(
                data["lastRun"]
            )
        )
    if "configurationSource" in data:
        import aws_sdk_glue.types.configuration_source

        out["configuration_source"] = (
            aws_sdk_glue.types.configuration_source.deserialize_aws_json_1_1(
                data["configurationSource"]
            )
        )
    return out
