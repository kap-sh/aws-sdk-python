"""Generated from Smithy shape ``com.amazonaws.glue#TargetTableConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_glue.types.integration_partition_spec_list
    import aws_sdk_glue.types.string128
    import aws_sdk_glue.types.unnest_spec


class TargetTableConfig(TypedDict):
    unnest_spec: NotRequired["aws_sdk_glue.types.unnest_spec.UnnestSpec"]
    r"""<p>Specifies how nested objects are flattened to top-level elements. Valid values are: \"TOPLEVEL\", \"FULL\", or \"NOUNNEST\".</p>"""
    partition_spec: NotRequired[
        "aws_sdk_glue.types.integration_partition_spec_list.IntegrationPartitionSpecList"
    ]
    """<p>Determines the file layout on the target.</p>"""
    target_table_name: NotRequired["aws_sdk_glue.types.string128.String128"]
    """<p>The optional name of a target table.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTableConfig) -> dict:
    out: dict = {}
    if "unnest_spec" in value:
        import aws_sdk_glue.types.unnest_spec

        out["UnnestSpec"] = aws_sdk_glue.types.unnest_spec.serialize_aws_json_1_1(
            value["unnest_spec"]
        )
    if "partition_spec" in value:
        import aws_sdk_glue.types.integration_partition_spec_list

        out["PartitionSpec"] = (
            aws_sdk_glue.types.integration_partition_spec_list.serialize_aws_json_1_1(
                value["partition_spec"]
            )
        )
    if "target_table_name" in value:
        out["TargetTableName"] = value["target_table_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetTableConfig:
    out: TargetTableConfig = {}  # type: ignore[typeddict-item]
    if "UnnestSpec" in data:
        import aws_sdk_glue.types.unnest_spec

        out["unnest_spec"] = aws_sdk_glue.types.unnest_spec.deserialize_aws_json_1_1(
            data["UnnestSpec"]
        )
    if "PartitionSpec" in data:
        import aws_sdk_glue.types.integration_partition_spec_list

        out["partition_spec"] = (
            aws_sdk_glue.types.integration_partition_spec_list.deserialize_aws_json_1_1(
                data["PartitionSpec"]
            )
        )
    if "TargetTableName" in data:
        out["target_table_name"] = data["TargetTableName"]
    return out
