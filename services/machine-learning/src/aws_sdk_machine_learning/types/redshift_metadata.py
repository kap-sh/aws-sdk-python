"""Generated from Smithy shape ``com.amazonaws.machinelearning#RedshiftMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.redshift_database
    import aws_sdk_machine_learning.types.redshift_database_username
    import aws_sdk_machine_learning.types.redshift_select_sql_query


class RedshiftMetadata(TypedDict):
    redshift_database: NotRequired[
        "aws_sdk_machine_learning.types.redshift_database.RedshiftDatabase"
    ]
    database_user_name: NotRequired[
        "aws_sdk_machine_learning.types.redshift_database_username.RedshiftDatabaseUsername"
    ]
    select_sql_query: NotRequired[
        "aws_sdk_machine_learning.types.redshift_select_sql_query.RedshiftSelectSqlQuery"
    ]
    """<p> The SQL query that is specified during <a>CreateDataSourceFromRedshift</a>. Returns only if <code>Verbose</code> is true in GetDataSourceInput. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftMetadata) -> dict:
    out: dict = {}
    if "redshift_database" in value:
        import aws_sdk_machine_learning.types.redshift_database

        out["RedshiftDatabase"] = (
            aws_sdk_machine_learning.types.redshift_database.serialize_aws_json_1_1(
                value["redshift_database"]
            )
        )
    if "database_user_name" in value:
        out["DatabaseUserName"] = value["database_user_name"]
    if "select_sql_query" in value:
        out["SelectSqlQuery"] = value["select_sql_query"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftMetadata:
    out: RedshiftMetadata = {}  # type: ignore[typeddict-item]
    if "RedshiftDatabase" in data:
        import aws_sdk_machine_learning.types.redshift_database

        out["redshift_database"] = (
            aws_sdk_machine_learning.types.redshift_database.deserialize_aws_json_1_1(
                data["RedshiftDatabase"]
            )
        )
    if "DatabaseUserName" in data:
        out["database_user_name"] = data["DatabaseUserName"]
    if "SelectSqlQuery" in data:
        out["select_sql_query"] = data["SelectSqlQuery"]
    return out
