"""Generated from Smithy shape ``com.amazonaws.kendra#ConnectionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kendra.types.database_host
    import aws_sdk_kendra.types.database_name
    import aws_sdk_kendra.types.database_port
    import aws_sdk_kendra.types.secret_arn
    import aws_sdk_kendra.types.table_name


class ConnectionConfiguration(TypedDict, closed=True):
    database_host: "aws_sdk_kendra.types.database_host.DatabaseHost"
    """<p>The name of the host for the database. Can be either a string (host.subdomain.domain.tld) or an IPv4 or IPv6 address.</p>"""
    database_port: "aws_sdk_kendra.types.database_port.DatabasePort"
    """<p>The port that the database uses for connections.</p>"""
    database_name: "aws_sdk_kendra.types.database_name.DatabaseName"
    """<p>The name of the database containing the document data.</p>"""
    table_name: "aws_sdk_kendra.types.table_name.TableName"
    """<p>The name of the table that contains the document data.</p>"""
    secret_arn: "aws_sdk_kendra.types.secret_arn.SecretArn"
    r"""<p>The Amazon Resource Name (ARN) of an Secrets Manager secret that stores the credentials. The credentials should be a user-password pair. For more information, see <a href=\"https://docs.aws.amazon.com/kendra/latest/dg/data-source-database.html\">Using a Database Data Source</a>. For more information about Secrets Manager, see <a href=\"https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html\"> What Is Secrets Manager</a> in the <i>Secrets Manager</i> user guide.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionConfiguration) -> dict:
    out: dict = {}
    out["DatabaseHost"] = value["database_host"]
    out["DatabasePort"] = value["database_port"]
    out["DatabaseName"] = value["database_name"]
    out["TableName"] = value["table_name"]
    out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionConfiguration:
    out: ConnectionConfiguration = {}  # type: ignore[typeddict-item]
    if "DatabaseHost" in data:
        out["database_host"] = data["DatabaseHost"]
    else:
        raise DeserializationError("ConnectionConfiguration.database_host required")
    if "DatabasePort" in data:
        out["database_port"] = data["DatabasePort"]
    else:
        raise DeserializationError("ConnectionConfiguration.database_port required")
    if "DatabaseName" in data:
        out["database_name"] = data["DatabaseName"]
    else:
        raise DeserializationError("ConnectionConfiguration.database_name required")
    if "TableName" in data:
        out["table_name"] = data["TableName"]
    else:
        raise DeserializationError("ConnectionConfiguration.table_name required")
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    else:
        raise DeserializationError("ConnectionConfiguration.secret_arn required")
    return out
