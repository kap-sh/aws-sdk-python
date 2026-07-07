"""Generated from Smithy shape ``com.amazonaws.rdsdata#RollbackTransactionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_rds_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_rds_data.types.arn
    import aws_sdk_rds_data.types.id


class RollbackTransactionRequest(TypedDict, closed=True):
    resource_arn: "aws_sdk_rds_data.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Aurora Serverless DB cluster.</p>"""
    secret_arn: "aws_sdk_rds_data.types.arn.Arn"
    """<p>The name or ARN of the secret that enables access to the DB cluster.</p>"""
    transaction_id: "aws_sdk_rds_data.types.id.Id"
    """<p>The identifier of the transaction to roll back.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RollbackTransactionRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["secretArn"] = value["secret_arn"]
    out["transactionId"] = value["transaction_id"]
    return out


def deserialize_json(data: dict) -> RollbackTransactionRequest:
    out: RollbackTransactionRequest = {}  # type: ignore[typeddict-item]
    if "resourceArn" in data:
        out["resource_arn"] = data["resourceArn"]
    else:
        raise DeserializationError("RollbackTransactionRequest.resource_arn required")
    if "secretArn" in data:
        out["secret_arn"] = data["secretArn"]
    else:
        raise DeserializationError("RollbackTransactionRequest.secret_arn required")
    if "transactionId" in data:
        out["transaction_id"] = data["transactionId"]
    else:
        raise DeserializationError("RollbackTransactionRequest.transaction_id required")
    return out
