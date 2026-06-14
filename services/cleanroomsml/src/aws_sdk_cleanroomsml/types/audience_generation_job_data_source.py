"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#AudienceGenerationJobDataSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.compute_configuration
    import aws_sdk_cleanroomsml.types.iam_role_arn
    import aws_sdk_cleanroomsml.types.protected_query_sql_parameters
    import aws_sdk_cleanroomsml.types.s3_config_map


class AudienceGenerationJobDataSource(TypedDict):
    data_source: NotRequired["aws_sdk_cleanroomsml.types.s3_config_map.S3ConfigMap"]
    r"""<p>Defines the Amazon S3 bucket where the seed audience for the generating audience is stored. A valid data source is a JSON line file in the following format:</p> <p> <code>{\"user_id\": \"111111\"}</code> </p> <p> <code>{\"user_id\": \"222222\"}</code> </p> <p> <code>...</code> </p>"""
    role_arn: "aws_sdk_cleanroomsml.types.iam_role_arn.IamRoleArn"
    """<p>The ARN of the IAM role that can read the Amazon S3 bucket where the seed audience is stored.</p>"""
    sql_parameters: NotRequired[
        "aws_sdk_cleanroomsml.types.protected_query_sql_parameters.ProtectedQuerySQLParameters"
    ]
    """<p>The protected SQL query parameters.</p>"""
    sql_compute_configuration: NotRequired[
        "aws_sdk_cleanroomsml.types.compute_configuration.ComputeConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: AudienceGenerationJobDataSource) -> dict:
    out: dict = {}
    if "data_source" in value:
        import aws_sdk_cleanroomsml.types.s3_config_map

        out["dataSource"] = aws_sdk_cleanroomsml.types.s3_config_map.serialize_json(
            value["data_source"]
        )
    out["roleArn"] = value["role_arn"]
    if "sql_parameters" in value:
        import aws_sdk_cleanroomsml.types.protected_query_sql_parameters

        out["sqlParameters"] = (
            aws_sdk_cleanroomsml.types.protected_query_sql_parameters.serialize_json(
                value["sql_parameters"]
            )
        )
    if "sql_compute_configuration" in value:
        import aws_sdk_cleanroomsml.types.compute_configuration

        out["sqlComputeConfiguration"] = (
            aws_sdk_cleanroomsml.types.compute_configuration.serialize_json(
                value["sql_compute_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> AudienceGenerationJobDataSource:
    out: AudienceGenerationJobDataSource = {}  # type: ignore[typeddict-item]
    if "dataSource" in data:
        import aws_sdk_cleanroomsml.types.s3_config_map

        out["data_source"] = aws_sdk_cleanroomsml.types.s3_config_map.deserialize_json(
            data["dataSource"]
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("AudienceGenerationJobDataSource.role_arn required")
    if "sqlParameters" in data:
        import aws_sdk_cleanroomsml.types.protected_query_sql_parameters

        out["sql_parameters"] = (
            aws_sdk_cleanroomsml.types.protected_query_sql_parameters.deserialize_json(
                data["sqlParameters"]
            )
        )
    if "sqlComputeConfiguration" in data:
        import aws_sdk_cleanroomsml.types.compute_configuration

        out["sql_compute_configuration"] = (
            aws_sdk_cleanroomsml.types.compute_configuration.deserialize_json(
                data["sqlComputeConfiguration"]
            )
        )
    return out
