"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#RedshiftDataParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.boolean
    import capo_cloudwatch_events.types.database
    import capo_cloudwatch_events.types.db_user
    import capo_cloudwatch_events.types.redshift_secret_manager_arn
    import capo_cloudwatch_events.types.sql
    import capo_cloudwatch_events.types.statement_name


class RedshiftDataParameters(TypedDict, closed=True):
    secret_manager_arn: NotRequired[
        "capo_cloudwatch_events.types.redshift_secret_manager_arn.RedshiftSecretManagerArn"
    ]
    """<p>The name or ARN of the secret that enables access to the database. Required when authenticating using Amazon Web Services Secrets Manager.</p>"""
    database: "capo_cloudwatch_events.types.database.Database"
    """<p>The name of the database. Required when authenticating using temporary credentials.</p>"""
    db_user: NotRequired["capo_cloudwatch_events.types.db_user.DbUser"]
    """<p>The database user name. Required when authenticating using temporary credentials.</p>"""
    sql: "capo_cloudwatch_events.types.sql.Sql"
    """<p>The SQL statement text to run.</p>"""
    statement_name: NotRequired[
        "capo_cloudwatch_events.types.statement_name.StatementName"
    ]
    """<p>The name of the SQL statement. You can name the SQL statement when you create it to identify the query.</p>"""
    with_event: "capo_cloudwatch_events.types.boolean.Boolean"
    """<p>Indicates whether to send an event back to EventBridge after the SQL statement runs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RedshiftDataParameters) -> dict:
    out: dict = {}
    if "secret_manager_arn" in value:
        out["SecretManagerArn"] = value["secret_manager_arn"]
    out["Database"] = value["database"]
    if "db_user" in value:
        out["DbUser"] = value["db_user"]
    out["Sql"] = value["sql"]
    if "statement_name" in value:
        out["StatementName"] = value["statement_name"]
    out["WithEvent"] = value.get("with_event", False)
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
    else:
        raise DeserializationError("RedshiftDataParameters.sql required")
    if "StatementName" in data:
        out["statement_name"] = data["StatementName"]
    if "WithEvent" in data:
        out["with_event"] = data["WithEvent"]
    else:
        out["with_event"] = False
    return out
