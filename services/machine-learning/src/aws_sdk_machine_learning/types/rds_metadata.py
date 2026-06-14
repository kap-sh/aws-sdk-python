"""Generated from Smithy shape ``com.amazonaws.machinelearning#RDSMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.edp_pipeline_id
    import aws_sdk_machine_learning.types.edp_resource_role
    import aws_sdk_machine_learning.types.edp_service_role
    import aws_sdk_machine_learning.types.rds_database
    import aws_sdk_machine_learning.types.rds_database_username
    import aws_sdk_machine_learning.types.rds_select_sql_query


class RDSMetadata(TypedDict):
    database: NotRequired["aws_sdk_machine_learning.types.rds_database.RDSDatabase"]
    """<p>The database details required to connect to an Amazon RDS.</p>"""
    database_user_name: NotRequired[
        "aws_sdk_machine_learning.types.rds_database_username.RDSDatabaseUsername"
    ]
    select_sql_query: NotRequired[
        "aws_sdk_machine_learning.types.rds_select_sql_query.RDSSelectSqlQuery"
    ]
    """<p>The SQL query that is supplied during <a>CreateDataSourceFromRDS</a>. Returns only if <code>Verbose</code> is true in <code>GetDataSourceInput</code>. </p>"""
    resource_role: NotRequired[
        "aws_sdk_machine_learning.types.edp_resource_role.EDPResourceRole"
    ]
    r"""<p>The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry out the copy task from Amazon RDS to Amazon S3. For more information, see <a href=\"https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html\">Role templates</a> for data pipelines.</p>"""
    service_role: NotRequired[
        "aws_sdk_machine_learning.types.edp_service_role.EDPServiceRole"
    ]
    r"""<p>The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see <a href=\"https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html\">Role templates</a> for data pipelines.</p>"""
    data_pipeline_id: NotRequired[
        "aws_sdk_machine_learning.types.edp_pipeline_id.EDPPipelineId"
    ]
    """<p>The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS to Amazon S3. You can use the ID to find details about the instance in the Data Pipeline console.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RDSMetadata) -> dict:
    out: dict = {}
    if "database" in value:
        import aws_sdk_machine_learning.types.rds_database

        out["Database"] = (
            aws_sdk_machine_learning.types.rds_database.serialize_aws_json_1_1(
                value["database"]
            )
        )
    if "database_user_name" in value:
        out["DatabaseUserName"] = value["database_user_name"]
    if "select_sql_query" in value:
        out["SelectSqlQuery"] = value["select_sql_query"]
    if "resource_role" in value:
        out["ResourceRole"] = value["resource_role"]
    if "service_role" in value:
        out["ServiceRole"] = value["service_role"]
    if "data_pipeline_id" in value:
        out["DataPipelineId"] = value["data_pipeline_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RDSMetadata:
    out: RDSMetadata = {}  # type: ignore[typeddict-item]
    if "Database" in data:
        import aws_sdk_machine_learning.types.rds_database

        out["database"] = (
            aws_sdk_machine_learning.types.rds_database.deserialize_aws_json_1_1(
                data["Database"]
            )
        )
    if "DatabaseUserName" in data:
        out["database_user_name"] = data["DatabaseUserName"]
    if "SelectSqlQuery" in data:
        out["select_sql_query"] = data["SelectSqlQuery"]
    if "ResourceRole" in data:
        out["resource_role"] = data["ResourceRole"]
    if "ServiceRole" in data:
        out["service_role"] = data["ServiceRole"]
    if "DataPipelineId" in data:
        out["data_pipeline_id"] = data["DataPipelineId"]
    return out
