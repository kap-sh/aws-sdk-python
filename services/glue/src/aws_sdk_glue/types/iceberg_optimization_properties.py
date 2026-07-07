"""Generated from Smithy shape ``com.amazonaws.glue#IcebergOptimizationProperties``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.iam_role_arn
    import aws_sdk_glue.types.parameters_map


class IcebergOptimizationProperties(TypedDict, closed=True):
    role_arn: NotRequired["aws_sdk_glue.types.iam_role_arn.IAMRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that will be assumed to perform Iceberg table optimization operations.</p>"""
    compaction: NotRequired["aws_sdk_glue.types.parameters_map.ParametersMap"]
    """<p>A map of key-value pairs that specify configuration parameters for Iceberg table compaction operations, which optimize the layout of data files to improve query performance.</p>"""
    retention: NotRequired["aws_sdk_glue.types.parameters_map.ParametersMap"]
    """<p>A map of key-value pairs that specify configuration parameters for Iceberg table retention operations, which manage the lifecycle of table snapshots to control storage costs.</p>"""
    orphan_file_deletion: NotRequired["aws_sdk_glue.types.parameters_map.ParametersMap"]
    """<p>A map of key-value pairs that specify configuration parameters for Iceberg orphan file deletion operations, which identify and remove files that are no longer referenced by the table metadata.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: IcebergOptimizationProperties) -> dict:
    out: dict = {}
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "compaction" in value:
        import aws_sdk_glue.types.parameters_map

        out["Compaction"] = aws_sdk_glue.types.parameters_map.serialize_aws_json_1_1(
            value["compaction"]
        )
    if "retention" in value:
        import aws_sdk_glue.types.parameters_map

        out["Retention"] = aws_sdk_glue.types.parameters_map.serialize_aws_json_1_1(
            value["retention"]
        )
    if "orphan_file_deletion" in value:
        import aws_sdk_glue.types.parameters_map

        out["OrphanFileDeletion"] = (
            aws_sdk_glue.types.parameters_map.serialize_aws_json_1_1(
                value["orphan_file_deletion"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> IcebergOptimizationProperties:
    out: IcebergOptimizationProperties = {}  # type: ignore[typeddict-item]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "Compaction" in data:
        import aws_sdk_glue.types.parameters_map

        out["compaction"] = aws_sdk_glue.types.parameters_map.deserialize_aws_json_1_1(
            data["Compaction"]
        )
    if "Retention" in data:
        import aws_sdk_glue.types.parameters_map

        out["retention"] = aws_sdk_glue.types.parameters_map.deserialize_aws_json_1_1(
            data["Retention"]
        )
    if "OrphanFileDeletion" in data:
        import aws_sdk_glue.types.parameters_map

        out["orphan_file_deletion"] = (
            aws_sdk_glue.types.parameters_map.deserialize_aws_json_1_1(
                data["OrphanFileDeletion"]
            )
        )
    return out
