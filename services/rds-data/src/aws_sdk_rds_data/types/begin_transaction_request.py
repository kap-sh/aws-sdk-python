"""Generated from Smithy shape ``com.amazonaws.rdsdata#BeginTransactionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_rds_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.arn
    import aws_sdk_rds_data.types.db_name


class BeginTransactionRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_rds_data.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.</p>"""
    secret_arn: "aws_sdk_rds_data.types.arn.Arn"
    """<p>The name or ARN of the secret that enables access to the DB cluster.</p>"""
    database: NotRequired["aws_sdk_rds_data.types.db_name.DbName"]
    """<p>The name of the database.</p>"""
    schema: NotRequired["aws_sdk_rds_data.types.db_name.DbName"]
    """<p>The name of the database schema.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BeginTransactionRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["secretArn"] = value["secret_arn"]
    if "database" in value:
        out["database"] = value["database"]
    if "schema" in value:
        out["schema"] = value["schema"]
    return out


def deserialize_json(data: dict) -> BeginTransactionRequest:
    out: BeginTransactionRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("BeginTransactionRequest.resource_arn required")
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError("BeginTransactionRequest.secret_arn required")
    if "database" in data:
        out["database"] = data["database"]
    if "schema" in data:
        out["schema"] = data["schema"]
    return out
