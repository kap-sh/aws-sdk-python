"""Generated from Smithy shape ``com.amazonaws.eventbridge#RedshiftDataParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_eventbridge.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_eventbridge.types.boolean
    import aws_sdk_eventbridge.types.database
    import aws_sdk_eventbridge.types.db_user
    import aws_sdk_eventbridge.types.redshift_secret_manager_arn
    import aws_sdk_eventbridge.types.sql
    import aws_sdk_eventbridge.types.sqls
    import aws_sdk_eventbridge.types.statement_name


class RedshiftDataParameters(TypedDict):
    secret_manager_arn: NotRequired[
        "aws_sdk_eventbridge.types.redshift_secret_manager_arn.RedshiftSecretManagerArn"
    ]
    """<p>The name or ARN of the secret that enables access to the database. Required when authenticating using Amazon Web Services Secrets Manager.</p>"""
    database: "aws_sdk_eventbridge.types.database.Database"
    """<p>The name of the database. Required when authenticating using temporary credentials.</p>"""
    db_user: NotRequired["aws_sdk_eventbridge.types.db_user.DbUser"]
    """<p>The database user name. Required when authenticating using temporary credentials.</p>"""
    sql: NotRequired["aws_sdk_eventbridge.types.sql.Sql"]
    """<p>The SQL statement text to run.</p>"""
    statement_name: NotRequired[
        "aws_sdk_eventbridge.types.statement_name.StatementName"
    ]
    """<p>The name of the SQL statement. You can name the SQL statement when you create it to identify the query.</p>"""
    with_event: "aws_sdk_eventbridge.types.boolean.Boolean"
    """<p>Indicates whether to send an event back to EventBridge after the SQL statement runs.</p>"""
    sqls: NotRequired["aws_sdk_eventbridge.types.sqls.Sqls"]
    """<p>One or more SQL statements to run. The SQL statements are run as a single transaction. They run serially in the order of the array. Subsequent SQL statements don't start until the previous statement in the array completes. If any SQL statement fails, then because they are run as one transaction, all work is rolled back.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftDataParameters) -> dict:
    out: dict = {}
    if "secret_manager_arn" in value:
        out["SecretManagerArn"] = value["secret_manager_arn"]
    out["Database"] = value["database"]
    if "db_user" in value:
        out["DbUser"] = value["db_user"]
    if "sql" in value:
        out["Sql"] = value["sql"]
    if "statement_name" in value:
        out["StatementName"] = value["statement_name"]
    out["WithEvent"] = value.get("with_event", False)
    if "sqls" in value:
        import aws_sdk_eventbridge.types.sqls

        out["Sqls"] = aws_sdk_eventbridge.types.sqls.serialize_aws_json_1_1(
            value["sqls"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RedshiftDataParameters:
    out: RedshiftDataParameters = {}  # type: ignore[typeddict-item]
    if "SecretManagerArn" in data:
        out["secret_manager_arn"] = data["SecretManagerArn"]
    if "Database" in data:
        out["database"] = data["Database"]
    else:
        raise DeserializationError("RedshiftDataParameters.database required")
    if "DbUser" in data:
        out["db_user"] = data["DbUser"]
    if "Sql" in data:
        out["sql"] = data["Sql"]
    if "StatementName" in data:
        out["statement_name"] = data["StatementName"]
    if "WithEvent" in data:
        out["with_event"] = data["WithEvent"]
    else:
        out["with_event"] = False
    if "Sqls" in data:
        import aws_sdk_eventbridge.types.sqls

        out["sqls"] = aws_sdk_eventbridge.types.sqls.deserialize_aws_json_1_1(
            data["Sqls"]
        )
    return out
