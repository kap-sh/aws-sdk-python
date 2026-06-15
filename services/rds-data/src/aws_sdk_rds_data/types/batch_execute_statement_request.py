"""Generated from Smithy shape ``com.amazonaws.rdsdata#BatchExecuteStatementRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.arn
    import aws_sdk_rds_data.types.db_name
    import aws_sdk_rds_data.types.id
    import aws_sdk_rds_data.types.sql_parameter_sets
    import aws_sdk_rds_data.types.sql_statement


class BatchExecuteStatementRequest(TypedDict):
    resource_arn: "aws_sdk_rds_data.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.</p>"""
    secret_arn: "aws_sdk_rds_data.types.arn.Arn"
    r"""<p>The ARN of the secret that enables access to the DB cluster. Enter the database user name and password for the credentials in the secret.</p> <p>For information about creating the secret, see <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_database_secret.html\">Create a database secret</a>.</p>"""
    sql: "aws_sdk_rds_data.types.sql_statement.SqlStatement"
    """<p>The SQL statement to run. Don't include a semicolon (;) at the end of the SQL statement.</p>"""
    database: NotRequired["aws_sdk_rds_data.types.db_name.DbName"]
    """<p>The name of the database.</p>"""
    schema: NotRequired["aws_sdk_rds_data.types.db_name.DbName"]
    """<p>The name of the database schema.</p> <note> <p>Currently, the <code>schema</code> parameter isn't supported.</p> </note>"""
    parameter_sets: NotRequired[
        "aws_sdk_rds_data.types.sql_parameter_sets.SqlParameterSets"
    ]
    """<p>The parameter set for the batch operation.</p> <p>The SQL statement is executed as many times as the number of parameter sets provided. To execute a SQL statement with no parameters, use one of the following options:</p> <ul> <li> <p>Specify one or more empty parameter sets.</p> </li> <li> <p>Use the <code>ExecuteStatement</code> operation instead of the <code>BatchExecuteStatement</code> operation.</p> </li> </ul> <note> <p>Array parameters are not supported.</p> </note>"""
    transaction_id: NotRequired["aws_sdk_rds_data.types.id.Id"]
    """<p>The identifier of a transaction that was started by using the <code>BeginTransaction</code> operation. Specify the transaction ID of the transaction that you want to include the SQL statement in.</p> <p>If the SQL statement is not part of a transaction, don't set this parameter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchExecuteStatementRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["secretArn"] = value["secret_arn"]
    out["sql"] = value["sql"]
    if "database" in value:
        out["database"] = value["database"]
    if "schema" in value:
        out["schema"] = value["schema"]
    if "parameter_sets" in value:
        import aws_sdk_rds_data.types.sql_parameter_sets

        out["parameterSets"] = aws_sdk_rds_data.types.sql_parameter_sets.serialize_json(
            value["parameter_sets"]
        )
    if "transaction_id" in value:
        out["transactionId"] = value["transaction_id"]
    return out


def deserialize_json(data: dict) -> BatchExecuteStatementRequest:
    out: BatchExecuteStatementRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("BatchExecuteStatementRequest.resource_arn required")
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError("BatchExecuteStatementRequest.secret_arn required")
    if "sql" in data:
        out["sql"] = data["sql"]
    else:
        raise DeserializationError("BatchExecuteStatementRequest.sql required")
    if "database" in data:
        out["database"] = data["database"]
    if "schema" in data:
        out["schema"] = data["schema"]
    if "parameterSets" in data:
        import aws_sdk_rds_data.types.sql_parameter_sets

        out["parameter_sets"] = (
            aws_sdk_rds_data.types.sql_parameter_sets.deserialize_json(
                data["parameterSets"]
            )
        )
    if "transactionId" in data:
        out["transaction_id"] = data["transactionId"]
    return out
